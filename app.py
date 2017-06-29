# -!- coding:utf-8 -!-
import re

from flask import Flask
from jinja2 import evalcontextfilter, Markup, escape

app = Flask(__name__)


@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    _paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


@app.template_filter()
@evalcontextfilter
def poiemoji(eval_ctx, text):
    result = []
    if 'Beifall' in text:
        result.append("👏")
    elif "Heiterkeit" in text:
        result.append("😂")
    elif "Unterbrechung" in text:
        result.append("⏰")
    else:
        result.append("🗯")
    result = " ".join(result)
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
