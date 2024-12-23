from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount
from dbClass import dbs
import sqlQrs, environ

templates = Jinja2Templates(directory='templates')

def getData(sql):
    out=[]
    with dbs() as db:
        with db.cursor as cursor:
            cursor.execute(sql)
            for row in cursor:
                out.append(row)
                #print(cursor.rownumber, cursor.arraysize, cursor.rowcount)
    return out


async def gridPage(request : Request):
    path = request.url.path
    loadUrl='loadOrders'
    return templates.TemplateResponse('index.j2', {'request' : request,
                                                    'loadUrl' : loadUrl,
                                                    })

async def orderData(request : Request):
    return JSONResponse(getData(sqlQrs.orderSQL))

routes = [    
    Route('/', gridPage),
    Route('/loadOrders', orderData),
    Mount('/css', StaticFiles(directory='css'), name='css'),
    Mount('/images', StaticFiles(directory='images'), name='images'),

]

app = Starlette(debug=environ.GetValue('DEBUG'), routes=routes)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app"
                 ,host=environ.GetValue('HOST')
                 ,port=environ.GetValue('PORT')
                 ,reload=environ.GetValue('RELOAD')
                 )