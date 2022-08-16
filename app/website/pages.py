from flask import Blueprint,request
import platform,socket,re,uuid,psutil

pages = Blueprint('pages', __name__)

@pages.route('/-/health')
def health():
	info={}
	try:
	    info['platform']=platform.system()
	    info['platform-release']=platform.release()
	    info['platform-version']=platform.version()
	    info['architecture']=platform.machine()
	    info['hostname']=socket.gethostname()
	    info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
	    info['processor']=platform.processor()
	    info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
	    info['health']='healthy'
	    return info
	except Exception as e:
		info['health']='unhealthy'
		return info, 500

@pages.route('/api/echo')
def login():
    text=request.args.get('text')
    info={}
    if text is None or text == "":
	    info['error']='error'
	    return info, 500
    else:
	    info['key']=text
	    return info