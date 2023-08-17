def app(event, context):
	print("hello from zappa")
	return {"body": "ok"}