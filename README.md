# أَثَرُهُم — Digital Sanad

منصة عرض تفاعلية لفكرة السند الرقمي للعلم والأثر.

## التشغيل المحلي

```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

ثم افتح:
`http://127.0.0.1:8000`

## Render

المشروع مصمم ليعمل كـ Docker Web Service. Render يقرأ `Dockerfile` ويشغّل أمر `CMD`، والتطبيق يستمع على `PORT` الذي توفره المنصة.

## ملاحظة

البيانات المعروضة في النسخة الحالية Demo data لأغراض العرض والتحكيم، وليست ادعاءات بحثية.
