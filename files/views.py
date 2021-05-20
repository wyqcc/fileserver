import json
import os

from django.http import JsonResponse
from django.shortcuts import render
import os

from fileserver.settings import paths
from django.views import View


def saveToFile(saveFile, content):
    try:

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
        type = json_obj['type']
        e_dict_type = {'tev': '', 'humiture': '', 'infra-red': ''}
        try:
            e_dict_type[type]
        except Exception as e:
            print(e)
            result = {'success': 450, 'message': '不接受这种数据类型'}
            return JsonResponse(result)
        if type == 'tev' or type == 'humiture':
            root = paths + 'tev(温度)\\{}\\'.format(json_obj['upload_time'])
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
                    file_name = type + '.' + json_obj['file_type']
                except Exception as e:
                    print(e)
                    result = {'success': 452, 'message': '不接受这种文件类型'}
                    return JsonResponse(result)
            data = json_obj['content']
            file_name = root + file_name
            if data:
                with open(file_name, 'w') as file_object:
                    file_object.write(data)
            else:
                result = {'success': 453, 'message': '数据为空'}
                return JsonResponse(result)
            result = {'success': 454, 'message': '上传成功'}
            return JsonResponse(result)
        else:
            site = json_obj['site']
            if site:
                root = paths + type + '\\{}\\{}\\'.format(site, json_obj['upload_time'])
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
                        file_name = type + '.' + json_obj['file_type']
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


class APIDownloadHandler(View):
    def get(self, request, img_name):
        context = {}
        context['img_name'] = img_name
        return render(request, 'runoob.html', context)


from fileserver.settings import BASE_DIR


class ALIFinalist(View):
    def get(self, request):

        print(request.getLocalName(),'获取本地名称，即服务器名称')
        print(request.getLocalPort(),'获取本地端口号，即Tomcat端口号')
        print(request.getLocale(),'用户的语言环境')
        print(request.getContextPath(),'context路径')
        print(request.getMethod(),'GET还是POST')
        print(request.getProtocol(),'协议，http协议')
        print(request.getQueryString(),'查询字符串')
        print(request.getRemoteAddr(),'远程IP，即客户端IP')
        print(request.getRemotePort(),'远程端口，即客户端端口')
        print(request.getRemoteUser(),'远程用户')
        print(request.getRequestedSessionId(),'客户端的Session的ID')
        print(request.getRequestURI(),'用户请求的URL')
        print(request.getScheme(),'协议头，例如http')
        print(request.getServerName(),'服务器名称')
        print(request.getServerPort(),'服务器端口')
        print(request.getServletPath(),'Servlet路径')



        dict_s = []
        for x in os.walk(BASE_DIR):
            sisete = {'name': x[0], 'catalogue': x[1], 'file': x[2]}
            dict_s.append(sisete)
        result = {'success': 460, 'data': dict_s}
        return JsonResponse(result)


def getFileInfo(infofile):
    info = {}
    info["isfile"] = os.path.isfile(infofile)
    info["isdir"] = os.path.isdir(infofile)
    info["size"] = os.path.getsize(infofile)
    info["atime"] = os.path.getatime(infofile)
    info["mtime"] = os.path.getmtime(infofile)
    info["ctime"] = os.path.getctime(infofile)
    info["name"] = os.path.basename(infofile)
    return info


class API_file(View):
    def get(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        filename = json_obj['filename']
        filename = paths + filename
        infofile = os.path.join(filename)
        if not os.path.isfile(infofile):
            result = {"success": 5023, "message": u"不是一个有效的文件"}
            return JsonResponse(result)
        result = {"success": 5024, "message": getFileInfo(infofile)}
        return JsonResponse(result)
