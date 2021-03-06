import json
from django.http import JsonResponse
from django.shortcuts import render
import os
from fileserver.settings import paths
from django.views import View
from fileserver.settings import BASE_DIR

file__url = BASE_DIR + '\static'


def saveToFile(saveFile, content):
    try:
        print(saveFile)
        tf = open(saveFile, 'w+b')
        tf.write(content)
        tf.close()
        os.rename(saveFile, saveFile)
        return True
    except Exception as e:
        print(e)
        return False


class APIUploadHandler(View):
    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        types = json_obj['type']
        e_list_type = ['tev', 'humiture', 'infra']
        if types in e_list_type:
            if types == 'tev' or types == 'humiture':
                root = paths + '/tev(温度)/{}/'.format(json_obj['upload_time'])
                if not os.path.exists(root):
                    os.makedirs(root)
                file_name = json_obj['file_name']
                if file_name:
                    try:
                        file_name = file_name + '.' + json_obj['file_type']
                    except Exception as e:
                        print(e)
                        result = {'success': 451, 'message': '不接受这种文件类型'}
                        return JsonResponse(result)
                else:
                    try:
                        file_name = types + '.' + json_obj['file_type']
                    except Exception as e:
                        print(e)
                        result = {'success': 452, 'message': '不接受这种文件类型'}
                        return JsonResponse(result)
                data = json_obj['content']
                file_name = root + file_name
                if data:
                    with open(file_name, 'w') as file_object:
                        print(file_name)
                        file_object.write(data)
                else:
                    result = {'success': 453, 'message': '数据为空'}
                    return JsonResponse(result)
                result = {'success': 454, 'message': '上传成功'}
                return JsonResponse(result)
            else:
                site = json_obj['site']
                if site:
                    root = paths + '/' + types + '/{}/{}/'.format(site, json_obj['upload_time'])
                    if not os.path.exists(root):
                        os.makedirs(root)
                    file_name = json_obj['image_name']
                    if file_name:
                        try:
                            file_name = file_name + '.' + json_obj['file_type']
                        except Exception as e:
                            print(e)
                            result = {'success': 455, 'message': '不接受这种文件类型'}
                            return JsonResponse(result)
                    else:
                        try:
                            file_name = types + '.' + json_obj['file_type']
                        except Exception as e:
                            print(e)
                            result = {'success': 456, 'message': '不接受这种文件类型'}
                            return JsonResponse(result)
                    data = json_obj['img_decode']
                    file_name = root + file_name
                    if data:
                        saveToFile(file_name, data)
                    else:
                        result = {'success': 457, 'message': '数据为空'}
                        return JsonResponse(result)
                    result = {'success': 458, 'message': '上传成功'}
                    return JsonResponse(result)
                else:
                    result = {'success': 459, 'message': '站点为空，或者数据异常'}
                    return JsonResponse(result)
        else:
            result = {'success': 450, 'message': '不接受这种数据类型'}
            return JsonResponse(result)


class APIDownloadHandler(View):
    def get(self, request, img_name):
        context = {'img_name': img_name}
        return render(request, 'runs.html', context)


class ALIFinalist(View):
    def get(self, request):
        list_s = []
        for x in os.walk(paths):
            dict_s = {'name': x[0], 'catalogue': x[1], 'file': x[2]}
            list_s.append(dict_s)
        result = {'success': 460, 'data': list_s}
        return JsonResponse(result)


def getFileInfo(infofile):
    info = {"isfile": os.path.isfile(infofile), "isdir": os.path.isdir(infofile), "size": os.path.getsize(infofile),
            "atime": os.path.getatime(infofile), "mtime": os.path.getmtime(infofile),
            "ctime": os.path.getctime(infofile), "name": os.path.basename(infofile)}
    return info


class API_file(View):
    def get(self, request):
        json_str = request.body
        json_obj = json.loads(json_str, strict=False)
        filename = json_obj['filename']
        info_file = os.path.join(filename)
        if not os.path.isfile(info_file):
            result = {"success": 5023, "message": u"不是一个有效的文件"}
            return JsonResponse(result)
        result = {"success": 5024, "message": getFileInfo(info_file)}
        return JsonResponse(result)


class Root_url(View):
    def get(self, request):
        result = {"success": 200, "message": paths}
        return JsonResponse(result)
