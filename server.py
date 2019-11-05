import os, sys
import sentry_sdk

from bottle import route, Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration


# sentry_sdk.init(
#     dsn="https://3cd9c6de8ee14236a190ab58cac72fe3@sentry.io/1804185",
#     integrations=[BottleIntegration()]
# )

 sentry_sdk.init(
    dsn="DSN",
    integrations=[BottleIntegration()]
)

@route("/")
def phrase():
  return "Well done!"

@route("/fail")  
def fail():  
    raise RuntimeError("HTTP 500 ERROR!")

@route("/success")
def success():
    return phrase()


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080)