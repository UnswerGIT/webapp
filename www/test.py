import orm 
from models import User,Blog,Comment
import asyncio



async def test():
	await orm.create_pool(loop=loop,host='127.0.0.1',port=3306,user='www-data',password='www-data',db='awesome')
	u=User(name='Test',email='test7@exmple.com',passwd='1234567890',image='about:blank')
	await u.save()
loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()