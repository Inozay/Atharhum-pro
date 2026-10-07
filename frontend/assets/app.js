const app = document.getElementById("app");
const nav = document.getElementById("nav");
const toast = document.getElementById("toast");
const routes = ["home","passport","verify","assistant","journey","impact"];

const icons = {passport:"◈",verify:"✓",assistant:"✦",journey:"◎",impact:"↗"};

function notify(text){
  toast.textContent=text; toast.classList.add("show");
  clearTimeout(window.__toast); window.__toast=setTimeout(()=>toast.classList.remove("show"),2400);
}

function shell(title, desc, body){
  return `<section class="page section">
    <div class="section-head"><span class="eyebrow">${title}</span><h2>${desc}</h2></div>${body}
  </section>`;
}

function home(){
 return `<div class="page">
  <section class="hero">
   <div>
    <span class="eyebrow"><i class="dot"></i> منصة السند الرقمي للعلم والأثر</span>
    <h1>من المعلومة<br><span class="gradient">إلى المعرفة الموثوقة</span></h1>
    <p class="lead">أَثَرُهُم يحوّل رحلة المعرفة من «معلومة وصلتني» إلى «معلومة يمكنني فهم أصلها والتحقق منها وتتبّع أثرها».</p>
    <div class="actions"><button class="primary" data-route="passport">ابدأ بجواز المحتوى ←</button><button class="secondary" data-route="verify">جرّب مركز التحقق</button></div>
    <div class="grid">
      <div class="stat"><strong>1,284</strong><span>أثر موثّق · بيانات عرض</span></div>
      <div class="stat"><strong>367</strong><span>مصدرًا مرتبطًا · بيانات عرض</span></div>
      <div class="stat"><strong>96%</strong><span>مؤشر ثقة تجريبي</span></div>
    </div>
   </div>
   <div class="trust-card">
    <div class="card-title"><b>قاعدة الثقة</b><span class="pill">النظام يعمل</span></div>
    <div class="ring"><div><strong>96</strong><small>Trust Index</small></div></div>
    <p style="color:var(--muted);line-height:1.9">الذكاء الاصطناعي يسرّع الوصول والفهم. لا يختصر المراجعة العلمية ولا ينتحل دورها.</p>
    <div class="result good">● آخر مزامنة: منذ 4 دقائق<br><small>Demo data · مؤشرات العرض توضيحية</small></div>
   </div>
  </section>
  <section class="section">
   <div class="section-head"><span class="eyebrow">كيف تعمل المنصة؟</span><h2>ثلاث طبقات تبني الثقة</h2><p>تجربة واحدة تبدأ بالمصدر وتنتهي بفهم قابل للتتبّع.</p></div>
   <div class="features">
    <div class="feature"><div class="icon">01</div><h3>السند</h3><p>تجميع المصدر والمرجع والسياق في بطاقة واحدة سهلة القراءة.</p></div>
    <div class="feature"><div class="icon">02</div><h3>التحقق</h3><p>فحص اتساق المحتوى ومؤشرات الثقة مع إظهار ما يحتاج مراجعة بشرية.</p></div>
    <div class="feature"><div class="icon">03</div><h3>الأثر</h3><p>تحويل المعرفة الموثوقة إلى رحلة تعلم ومؤشرات أثر قابلة للفهم.</p></div>
   </div>
  </section>
 </div>`;
}

function passport(){
 return shell("◈ جواز المحتوى","بطاقة هوية رقمية للمعلومة",`
 <div class="split">
  <div class="section-card">
   <div class="card-title"><b>أثر: «أهمية الإسناد في نقل المعرفة»</b><span class="pill">موثّق</span></div>
   <p style="color:var(--muted);line-height:1.9">نموذج تجريبي يوضح كيف تتحول المعلومة إلى سجل قابل للتتبّع، مع مصدر وسياق ومؤشر ثقة.</p>
   <table class="table"><tr><th>العنصر</th><th>الحالة</th></tr><tr><td>المصدر</td><td>✓ مرتبط</td></tr><tr><td>السياق</td><td>✓ متاح</td></tr><tr><td>المراجعة</td><td>✓ مكتملة تجريبيًا</td></tr></table>
  </div>
  <div class="section-card">
   <div class="card-title"><b>معرّف الأثر</b><span style="color:var(--gold)">ATH-2048</span></div>
   <div class="score">96<span style="font-size:15px;color:var(--muted)"> / 100</span></div>
   <p style="color:var(--muted)">مؤشر ثقة تجريبي</p><div class="progress"><i style="width:96%"></i></div>
   <div class="actions"><button class="primary" id="copyId">نسخ المعرّف</button><button class="secondary" data-route="verify">التحقق من الأثر</button></div>
  </div>
 </div>`);
}

function verify(){
 return shell("✓ مركز التحقق","اختبر محتوى قبل أن تبني عليه معرفة",`
 <div class="section-card">
  <label>ألصق نصًا أو فكرة للتحقق منها</label>
  <textarea id="verifyText" class="field" placeholder="مثال: اكتب هنا معلومة تريد فحص بنيتها ومصادرها..."></textarea>
  <div class="actions"><button class="primary" id="runVerify">بدء الفحص</button><button class="secondary" id="sampleVerify">استخدم مثالًا</button></div>
  <div id="verifyResult" class="result">لم يبدأ الفحص بعد. هذه تجربة توضيحية وليست حكمًا علميًا نهائيًا.</div>
 </div>`);
}

function assistant(){
 return shell("✦ المساعد الموثق","اسأل، ثم شاهد أساس الإجابة",`
 <div class="section-card chat">
  <div id="messages" class="messages">
   <div class="msg bot">مرحبًا. أنا المساعد الموثق في أَثَرُهُم. سأوضح لك <b>ما نعرفه</b> و<b>ما يحتاج إلى مراجعة</b> بدل تقديم الثقة الزائفة.</div>
  </div>
  <div class="chatbar"><input id="chatInput" class="field" placeholder="اكتب سؤالك..."><button class="primary" id="sendChat">إرسال</button></div>
 </div>`);
}

function journey(){
 return shell("◎ رحلة التعلم","من الفضول إلى الفهم",`
 <div class="steps">
  <div class="step"><div class="num">01</div><div><b>اكتشف</b><p style="color:var(--muted)">اختر أثرًا أو موضوعًا تريد فهمه.</p></div></div>
  <div class="step"><div class="num">02</div><div><b>افهم السند</b><p style="color:var(--muted)">شاهد المصدر والسياق وعلاقة العناصر ببعضها.</p></div></div>
  <div class="step"><div class="num">03</div><div><b>تحقق</b><p style="color:var(--muted)">راجع مؤشرات الثقة وحدود النتيجة.</p></div></div>
  <div class="step"><div class="num">04</div><div><b>اترك أثرًا</b><p style="color:var(--muted)">سجّل ما تعلمته وابنِ مسارًا معرفيًا قابلًا للتتبّع.</p></div></div>
 </div>`);
}

function impact(){
 return shell("↗ ذكاء الأثر","لوحة أثر واضحة للجنة والمستخدم",`
 <div class="grid">
  <div class="stat"><strong>942</strong><span>متعلمًا في النموذج</span></div>
  <div class="stat"><strong>3.8×</strong><span>تحسن تجريبي في سرعة الوصول</span></div>
  <div class="stat"><strong>87%</strong><span>اكتمال مسارات التعلم</span></div>
 </div>
 <div class="split" style="margin-top:18px">
  <div class="section-card"><div class="card-title"><b>رحلة المستخدم</b><span class="pill">Demo</span></div><p style="color:var(--muted)">اكتشاف → سند → تحقق → تعلم</p><div class="progress"><i style="width:82%"></i></div></div>
  <div class="section-card"><div class="card-title"><b>مبدأ القياس</b></div><p style="color:var(--muted);line-height:2">لا نعرض الأرقام كحقائق بحثية. كل مؤشر في النسخة التحكيمية معلّم بوضوح بأنه Demo data.</p></div>
 </div>`);
}

function render(route=location.hash.slice(1)||"home"){
 if(!routes.includes(route)) route="home";
 const views={home,passport,verify,assistant,journey,impact};
 app.innerHTML=views[route]();
 document.querySelectorAll("[data-route]").forEach(b=>b.addEventListener("click",()=>navigate(b.dataset.route)));
 nav.querySelectorAll("button[data-route]").forEach(b=>b.classList.toggle("active",b.dataset.route===route));
 window.scrollTo({top:0,behavior:"smooth"});
 bind();
}

function navigate(route){location.hash=route}
window.addEventListener("hashchange",()=>render());

function bind(){
 document.querySelectorAll("[data-route]").forEach(b=>b.addEventListener("click",()=>navigate(b.dataset.route)));
 const copy=document.getElementById("copyId");
 if(copy) copy.onclick=async()=>{try{await navigator.clipboard.writeText("ATH-2048");notify("تم نسخ معرّف الأثر")}catch{notify("المعرّف: ATH-2048")}};
 const sample=document.getElementById("sampleVerify");
 if(sample) sample.onclick=()=>{document.getElementById("verifyText").value="هذه معلومة تجريبية لاختبار رحلة التحقق في أَثَرُهُم."};
 const run=document.getElementById("runVerify");
 if(run) run.onclick=()=>{
   const text=document.getElementById("verifyText").value.trim();
   const out=document.getElementById("verifyResult");
   if(!text){out.className="result warn";out.innerHTML="⚠️ أدخل نصًا أولًا حتى نبدأ الفحص.";return}
   out.className="result good";out.innerHTML=`<b>✓ اكتمل الفحص التجريبي</b><br>تم تحليل بنية المحتوى (${text.length} حرفًا).<br><span style="color:var(--muted)">النتيجة: يحتاج ربطًا بمصادر أولية قبل اعتباره موثّقًا.</span>`;
 };
 const send=document.getElementById("sendChat");
 if(send) send.onclick=sendMessage;
 const input=document.getElementById("chatInput");
 if(input) input.addEventListener("keydown",e=>{if(e.key==="Enter")sendMessage()});
}

function sendMessage(){
 const input=document.getElementById("chatInput"); if(!input||!input.value.trim())return;
 const box=document.getElementById("messages"); const q=input.value.trim();
 box.innerHTML+=`<div class="msg user">${escapeHtml(q)}</div>`;
 setTimeout(()=>{box.innerHTML+=`<div class="msg bot">إجابة تجريبية موثّقة: أستطيع مساعدتك في تفكيك السؤال وتحديد المصادر المطلوبة، لكن لا أقدّم هذه الإجابة كحكم علمي نهائي دون مراجعة المصدر الأصلي.</div>`;box.scrollTop=box.scrollHeight},350);
 input.value="";box.scrollTop=box.scrollHeight;
}
function escapeHtml(s){return s.replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]))}

document.getElementById("demoBtn").onclick=()=>{
 navigate("home"); setTimeout(()=>notify("وضع لجنة التحكيم جاهز — ابدأ من جواز المحتوى"),200);
};
document.getElementById("menuBtn").onclick=()=>nav.classList.toggle("open");
render();
