from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from pathlib import Path
from datetime import datetime, timezone
import re

ROOT = Path(__file__).resolve().parents[1]
app = FastAPI(title='Atharhum — Digital Chain of Trusted Knowledge', version='2.0.0')

CONTENT = [
    {
        'id':'AH-001','title':'خلق المسلم في العصر الرقمي','category':'أخلاق','language':'العربية',
        'source':'مصدر موثوق — مادة مؤسسية مُراجعة','edition':'الإصدار 1.4','version':'1.4',
        'status':'verified','review':'مراجعة بشرية مكتملة','reviewer':'مراجع علمي معتمد',
        'updated':'2026-09-18','summary':'مادة تعليمية تربط قيمة الأمانة بسلوك الإنسان في البيئة الرقمية، مع توضيح أن حفظ الأثر يشمل حفظ المصدر والسياق.',
        'tags':['الأمانة','الأثر','المسؤولية الرقمية'],
        'provenance':[
            ('الأصل','المصدر المعتمد','2026-08-20','verified'),
            ('المراجعة','مراجعة بشرية','2026-08-23','verified'),
            ('الإصدار','تنقيح وإثبات النسخة 1.4','2026-09-18','verified'),
            ('الترجمة','صياغة إنجليزية مرتبطة بالأصل','2026-09-20','verified'),
            ('النشر','منصة أَثَرُهُم','2026-09-21','verified')],
        'evidence':['هوية المحتوى AH-001','سجل مراجعة بشري','سلسلة الإصدارات','علاقة الترجمة بالأصل']
    },
    {
        'id':'AH-002','title':'كيف نتحقق من المعلومة قبل نشرها؟','category':'منهجية','language':'العربية',
        'source':'مقالة إرشادية — مراجعة تحريرية','edition':'الإصدار 2.1','version':'2.1',
        'status':'verified','review':'مراجعة بشرية مكتملة','reviewer':'فريق التحقق','updated':'2026-09-11',
        'summary':'إطار عملي لفحص الأصل والسياق والإصدار والمراجعة قبل إعادة استخدام أي مادة معرفية رقمية.',
        'tags':['تحقق','مصادر','سياق'],
        'provenance':[
            ('الأصل','وثيقة إرشادية','2026-07-11','verified'),('المراجعة','فريق التحقق','2026-07-14','verified'),
            ('الإصدار','الإصدار 2.1','2026-09-11','verified'),('النشر','منصة أَثَرُهُم','2026-09-12','verified')],
        'evidence':['مصدر محدد','سجل مراجعة','نسخة حالية','معرّف تحقق AH-002']
    },
    {
        'id':'AH-003','title':'من المصدر إلى المتعلم: رحلة المعرفة','category':'تعلم','language':'العربية',
        'source':'وحدة تعليمية — مراجعة منهجية','edition':'الإصدار 1.0','version':'1.0','status':'verified',
        'review':'مراجعة بشرية مكتملة','reviewer':'مراجع المنهج','updated':'2026-09-04',
        'summary':'وحدة تشرح كيف تتحول المعرفة الموثقة إلى رحلة تعلم قابلة للقياس دون فقدان الأصل أو السياق.',
        'tags':['تعلم','رحلة','أثر'],
        'provenance':[
            ('الأصل','مادة تعليمية أصلية','2026-08-01','verified'),('المراجعة','مراجع المنهج','2026-08-03','verified'),
            ('التعليم','تحويلها إلى دروس قصيرة','2026-08-15','verified'),('النشر','منصة أَثَرُهُم','2026-08-16','verified')],
        'evidence':['أهداف تعلم','دروس قصيرة','اختبار فهم','سجل تقدم']
    }
]

KNOWLEDGE = {
    'الأمانة': 'الأمانة هنا لا تعني فقط صحة العبارة، بل الحفاظ على نسبتها وسياقها وعدم فصلها عن مسارها. لذلك يربط أَثَرُهُم المحتوى بمصدره وإصداره ومراجعته.',
    'التحقق': 'التحقق في أَثَرُهُم يبدأ من هوية المحتوى ثم المصدر والإصدار والمراجعة، وبعدها يمكن تتبع الترجمات والنسخ المشتقة بدل التعامل معها كمواد منفصلة.',
    'الأثر': 'الأثر يقيس ما يحدث بعد الوصول: هل تم فتح جواز المحتوى؟ هل تم التحقق من المصدر؟ هل بدأت رحلة تعلم؟ هل اكتملت؟ هل أعيد استخدام المعرفة؟ ثم تُجمع الإشارات بصورة تحافظ على الخصوصية.',
    'الذكاء الاصطناعي': 'المساعد الموثق لا يُعامل كبديل عن أهل الاختصاص. وظيفته استرجاع المعرفة المرتبطة بالمصادر، شرحها، ربطها بالسياق، وإظهار الأدلة التي بُنيت عليها الإجابة.',
    'السند': 'السند الرقمي هو سجل قابل للتتبع يربط الأصل بالمراجعة والإصدار والترجمة والنسخ المشتقة. الهدف هو ألا تفقد المعرفة قصتها أثناء انتقالها رقمياً.'
}

class AskRequest(BaseModel):
    question: str = ''
    content_id: str | None = None

class VerifyRequest(BaseModel):
    content_id: str

class EventRequest(BaseModel):
    event: str
    content_id: str = 'AH-001'

@app.get('/api/health')
def health():
    return {'ok': True, 'service':'atharhum', 'version':'2.0.0', 'time':datetime.now(timezone.utc).isoformat()}

@app.get('/api/content')
def content():
    return CONTENT

@app.get('/api/content/{content_id}')
def content_one(content_id: str):
    item = next((x for x in CONTENT if x['id'].upper()==content_id.upper()), None)
    if not item: raise HTTPException(404, 'المحتوى غير موجود')
    return item

@app.post('/api/verify')
def verify(req: VerifyRequest):
    item = next((x for x in CONTENT if x['id'].upper()==req.content_id.upper()), None)
    if not item: return {'verified':False,'message':'لم يتم العثور على هوية محتوى بهذا المعرّف.'}
    return {'verified':True,'id':item['id'],'title':item['title'],'status':item['status'],'version':item['version'],'review':item['review'],'source':item['source']}

@app.post('/api/ask')
def ask(req: AskRequest):
    q = req.question.strip()
    if not q: return {'answer':'اكتب سؤالًا لأبدأ الاسترجاع من قاعدة المعرفة الموثقة.','sources':[],'grounded':True}
    low = q.lower()
    ranked=[]
    for item in CONTENT:
        hay = ' '.join([item['title'],item['summary'],item['category'],' '.join(item['tags'])]).lower()
        score = sum(1 for token in re.findall(r'[\w\u0600-\u06ff]+', low) if len(token)>2 and token in hay)
        if req.content_id and item['id']==req.content_id: score += 3
        ranked.append((score,item))
    ranked.sort(key=lambda x:x[0], reverse=True)
    selected=[x[1] for x in ranked[:2]]
    if any(k in low for k in KNOWLEDGE):
        matches=[(k,v) for k,v in KNOWLEDGE.items() if k in low]
        answer=matches[0][1]
    elif selected and ranked[0][0]>0:
        answer=selected[0]['summary']+' ويمكن تتبع أصل هذه المادة ومراجعتها وإصدارها من جواز المحتوى.'
    else:
        answer='لم أجد إجابة موثقة كافية داخل قاعدة المعرفة الحالية. أَثَرُهُم يفضّل إظهار حدود المعرفة بدل توليد إجابة بلا سند. جرّب سؤالًا عن الأمانة أو التحقق أو السند أو الأثر.'
        selected=[]
    return {'answer':answer,'sources':[{'id':x['id'],'title':x['title'],'version':x['version']} for x in selected], 'grounded':True,'mode':'source-grounded','confidence':'مرتفع' if selected else 'غير كافٍ'}

@app.post('/api/event')
def event(req: EventRequest):
    allowed={'view':1,'passport':1,'verify':1,'ask':1,'lesson_start':1,'lesson_complete':1,'reuse':1,'share':1}
    return {'accepted':req.event in allowed,'event':req.event,'content_id':req.content_id,'recorded_at':datetime.now(timezone.utc).isoformat(),'privacy':'aggregated'}

@app.get('/api/impact')
def impact():
    return {'funnel':[{'key':'reach','label':'الوصول','value':12840},{'key':'verify','label':'التحقق','value':8740},{'key':'learn','label':'التعلم','value':6110},{'key':'complete','label':'الإكمال','value':4280},{'key':'reuse','label':'إعادة الاستخدام','value':2190},{'key':'impact','label':'إشارة أثر','value':1360}], 'note':'بيانات تشغيلية تجريبية داخل المنتج وليست نتائج بحثية.'}

@app.get('/')
def root():
    return FileResponse(ROOT/'frontend'/'index.html')

app.mount('/static', StaticFiles(directory=ROOT/'frontend'/'static'), name='static')
