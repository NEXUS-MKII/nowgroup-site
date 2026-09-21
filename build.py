import io,json,re,html as H,os
T=json.load(io.open('testimonials.json',encoding='utf-8'))
IMG='https://nexus-mkii.github.io/nowgroup-site/img/'
FONT='https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Barlow:wght@400;500;600&family=Blinker:wght@300;400;600&display=swap'

BASE = r"""
  :root{--ground:#F5F5F7;--paper:#FFFFFF;--ink:#0B0A0A;--ink-2:#2A2628;--orange:#F03808;--orange-deep:#C82E06;--mut:#6B6670;--line:#E3E1E6;--dark:#0F0D0D;--console:#080808;--pq-void:#17110A;--pq-gold:#E6BE6A;--pq-silver:#C9CFD6;}
  .nw,.nw *,.nw *::before,.nw *::after{box-sizing:border-box;margin:0;padding:0;}
  .nw{font-family:'Blinker',system-ui,sans-serif;font-weight:300;font-size:17px;line-height:1.6;color:var(--ink);background:var(--ground);-webkit-font-smoothing:antialiased;text-align:left;}
  .nw h1,.nw h2,.nw h3,.nw p{margin:0;} .nw a{color:inherit;text-decoration:none;} .nw img{max-width:100%;}
  .nw .disp{font-family:'Barlow Condensed',sans-serif;font-weight:700;text-transform:uppercase;line-height:.94;letter-spacing:-.005em;text-wrap:balance;}
  .nw .eye{font-family:'Barlow',sans-serif;font-weight:600;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--orange);}
  .nw .wrap{max-width:1120px;margin:0 auto;padding:0 clamp(20px,5vw,56px);}
  .nw section{padding:clamp(72px,9vw,128px) 0;}
  .nw .lede{font-weight:400;font-size:clamp(18px,1.6vw,21px);line-height:1.55;color:var(--ink-2);max-width:56ch;}
  .nw .body{max-width:62ch;color:var(--ink-2);font-size:17px;} .nw .body + .body{margin-top:1.1em;} .nw .body b{font-weight:600;color:var(--ink);}
  .nw :focus-visible{outline:2px solid var(--orange);outline-offset:3px;}
  .nw .btn{display:inline-flex;align-items:center;gap:12px;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:19px;text-transform:uppercase;letter-spacing:.04em;padding:17px 34px;border-radius:4px;cursor:pointer;background:var(--orange);color:#fff;border:2px solid var(--orange);transition:transform .15s,background .15s,border-color .15s,box-shadow .15s;box-shadow:0 10px 30px rgba(240,56,8,.22);}
  .nw .btn:hover{background:var(--orange-deep);border-color:var(--orange-deep);transform:translateY(-2px);}
  .nw .btn .arr{font-family:'Barlow',sans-serif;font-weight:400;}
  .nw .btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.7);box-shadow:none;} .nw .btn-ghost:hover{background:#fff;color:var(--ink);border-color:#fff;}
  .nw .two{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(32px,6vw,80px);align-items:start;} @media(max-width:820px){.nw .two{grid-template-columns:1fr;}}
  html.js .nw .rv{opacity:0;transform:translateY(18px);} html.js .nw .rv.in{opacity:1;transform:none;transition:opacity .7s ease,transform .8s cubic-bezier(.2,.8,.2,1);}
  .nw .console{background:var(--console);color:#fff;position:relative;overflow:hidden;}
  .nw .console::before{content:'';position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.08) 2px,rgba(0,0,0,.08) 4px);pointer-events:none;z-index:0;}
  .nw .console .glow{position:absolute;pointer-events:none;z-index:0;filter:blur(18px);background:radial-gradient(ellipse,rgba(240,56,8,.10) 0%,transparent 65%);}
  .nw .console .wrap{position:relative;z-index:1;} .nw .console .eye{color:var(--orange);}
  .nw .frame{position:relative;border:1.5px solid rgba(240,56,8,.32);border-radius:12px;overflow:hidden;background:#0a0a0a;box-shadow:0 0 0 1px rgba(240,56,8,.07),0 0 48px rgba(240,56,8,.05),0 28px 68px rgba(0,0,0,.68);}
  .nw .frame .ctl,.nw .frame .cbr{position:absolute;width:14px;height:14px;pointer-events:none;z-index:3;}
  .nw .frame .ctl{top:-1px;left:-1px;border-top:2px solid var(--orange);border-left:2px solid var(--orange);border-radius:2px 0 0 0;}
  .nw .frame .cbr{bottom:-1px;right:-1px;border-bottom:2px solid var(--orange);border-right:2px solid var(--orange);border-radius:0 0 2px 0;}
  .nw .chrome{display:flex;align-items:center;justify-content:space-between;padding:9px 16px;background:#0d0d0d;border-bottom:1px solid rgba(240,56,8,.18);gap:10px;}
  .nw .chrome .dots{display:flex;gap:5px;flex-shrink:0;} .nw .chrome .dots i{width:9px;height:9px;border-radius:50%;display:block;}
  .nw .chrome .ct{font-family:'Barlow',sans-serif;font-size:10px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.25);text-align:center;flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
  .nw .chrome .led{display:flex;align-items:center;gap:6px;flex-shrink:0;font-family:'Barlow',sans-serif;font-size:10px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(240,56,8,.7);}
  .nw .chrome .led i{width:6px;height:6px;border-radius:50%;background:var(--orange);display:block;animation:nwled 2s ease-in-out infinite;}
  @keyframes nwled{0%,100%{opacity:1;}50%{opacity:.25;}}
  @media(prefers-reduced-motion:reduce){.nw *{animation:none!important;transition:none!important;} html.js .nw .rv{opacity:1!important;transform:none!important;}}
"""
OVERRIDE = """<style>
  .c-section:has(.nw) > .inner{max-width:none!important;width:100%!important;}
  .c-section:has(.nw),.c-section:has(.nw) .c-row,.c-section:has(.nw) .c-column{padding:0!important;margin:0!important;}
  body{background:#F5F5F7!important;}
</style>
"""
JSHEAD = "<script>document.documentElement.className+=' js';</script>\n"
FINDROOT = "  var s=document.currentScript, root=s&&s.previousElementSibling; while(root && !(root.classList&&root.classList.contains('nw'))) root=root.previousElementSibling;\n  if(!root) return;\n"
REVEAL = """  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els=[].slice.call(root.querySelectorAll('.rv'));
  if(reduce||!('IntersectionObserver' in window)){ els.forEach(function(e){e.classList.add('in');}); }
  else{ var io=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.18}); els.forEach(function(e){io.observe(e);}); }
  var JOIN_URL=''; /* <- the GHL order form / checkout URL */
  [].forEach.call(root.querySelectorAll('[data-cta="join"]'),function(a){ if(JOIN_URL) a.setAttribute('href',JOIN_URL); });
"""

CSS1 = r"""
  .nw .nav{position:relative;z-index:5;display:flex;align-items:center;justify-content:space-between;padding:16px 0;}
  .nw .mark img{display:block;height:58px;width:auto;}
  .nw .navl{display:flex;gap:clamp(18px,3vw,34px);align-items:center;font-family:'Barlow',sans-serif;font-weight:500;font-size:14px;letter-spacing:.08em;text-transform:uppercase;color:rgba(255,255,255,.82);}
  .nw .navl a:hover{color:var(--orange);} .nw .navl .btn{padding:11px 20px;font-size:15px;box-shadow:none;}
  @media(max-width:640px){.nw .navl a:not(.btn){display:none;}}
  .nw .hero{background:var(--dark);color:#fff;padding-top:0;padding-bottom:0;position:relative;overflow:hidden;}
  .nw .hero .bg{position:absolute;inset:0;z-index:0;background:url(IMGhero-floor.webp) center 40%/cover no-repeat;opacity:.55;}
  .nw .hero .bg::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,13,13,.96) 0%,rgba(15,13,13,.82) 45%,rgba(15,13,13,.35) 100%),linear-gradient(180deg,rgba(15,13,13,.9),transparent 30%,transparent 70%,rgba(15,13,13,.95));}
  .nw .hero .wrap{position:relative;z-index:1;}
  .nw .hero-in{padding:clamp(56px,8vw,112px) 0 clamp(72px,9vw,124px);display:grid;grid-template-columns:minmax(0,1fr) auto;gap:40px;align-items:center;}
  .nw .hero h1{font-size:clamp(48px,7.2vw,104px);color:#fff;max-width:13.5ch;} .nw .hero h1 em{font-style:normal;color:var(--orange);}
  .nw br.wide{display:none;} @media(min-width:761px){.nw br.wide{display:inline;}}
  .nw .hero .lede{margin-top:26px;color:rgba(255,255,255,.8);}
  .nw .hero .acts{margin-top:36px;display:flex;gap:14px;flex-wrap:wrap;align-items:center;}
  .nw .hero .fine{margin-top:18px;font-family:'Barlow',sans-serif;font-size:13px;letter-spacing:.06em;color:rgba(255,255,255,.55);text-transform:uppercase;}
  .nw .stamp{position:relative;width:clamp(170px,19vw,250px);aspect-ratio:1;border:4px solid var(--orange);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--orange);transform:rotate(-12deg);font-family:'Barlow Condensed',sans-serif;text-transform:uppercase;line-height:.86;box-shadow:inset 0 0 0 3px var(--dark),inset 0 0 0 5px var(--orange);-webkit-mask-image:radial-gradient(circle at 30% 30%,#000 62%,rgba(0,0,0,.86) 100%);mask-image:radial-gradient(circle at 30% 30%,#000 62%,rgba(0,0,0,.86) 100%);}
  .nw .stamp b{font-weight:800;font-size:clamp(66px,7.6vw,102px);letter-spacing:-.02em;}
  .nw .stamp b sup{font-size:.42em;vertical-align:top;position:relative;top:.16em;}
  .nw .stamp span{font-weight:700;font-size:clamp(15px,1.5vw,20px);letter-spacing:.24em;margin-top:2px;}
  .nw .stamp small{font-family:'Barlow',sans-serif;font-weight:600;font-size:10px;letter-spacing:.16em;margin-top:8px;color:#fff;}
  html.js .nw .stamp{opacity:0;transform:rotate(-12deg) scale(1.35);}
  html.js .nw .hero.in .stamp{opacity:1;transform:rotate(-12deg) scale(1);transition:opacity .35s ease .5s,transform .45s cubic-bezier(.2,1.2,.3,1) .5s;}
  @media(max-width:760px){.nw .hero-in{grid-template-columns:1fr;}.nw .stamp{margin:0 auto;}}
  @media(prefers-reduced-motion:reduce){html.js .nw .stamp{opacity:1!important;transform:rotate(-12deg)!important;}}
""".replace('IMG',IMG)
HTML1 = r"""  <section class="hero">
    <div class="bg" aria-hidden="true"></div>
    <div class="wrap">
      <nav class="nav" aria-label="Main">
        <a class="mark" href="/" aria-label="The NOW Group"><img src="IMGlogo-dark.png" alt="The NOW Group" width="562" height="456"></a>
        <div class="navl"><a href="/about">About</a><a href="#how">How it works</a><a href="#faq">FAQ</a><a class="btn" href="#" data-cta="join">Join for $50</a></div>
      </nav>
      <div class="hero-in">
        <div>
          <div class="eye">NOW Group &middot; NZ &amp; AU &middot; an open meeting</div>
          <h1 class="disp" style="margin-top:18px">Paid networking is broken.<br class="wide"> <em>So we stopped selling it.</em></h1>
          <p class="lede">One open meeting. Fifty dollars, once. A year of access. No tiers, no upgrades, no obligations &mdash; and nobody performing.</p>
          <div class="acts"><a class="btn" href="#" data-cta="join">Join for $50 <span class="arr">&rarr;</span></a><a class="btn btn-ghost" href="#how">How it works</a></div>
          <div class="fine">Pay once &middot; NET_SYNC in ten minutes &middot; one Zoom link, valid a year</div>
        </div>
        <div class="stamp" aria-hidden="true"><b><sup>$</sup>50</b><span>Once</span><small>12 months &middot; no renewal</small></div>
      </div>
    </div>
  </section>
""".replace('IMG',IMG)
JS1 = "(function(){\n"+FINDROOT+"  var hero=root.querySelector('.hero'); var rm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;\n  if(hero){ if(rm) hero.classList.add('in'); else setTimeout(function(){hero.classList.add('in');},80); }\n"+REVEAL+"})();"

CSS2 = r"""
  .nw .thesis{background:var(--ground);border-top:1px solid var(--line);border-bottom:1px solid var(--line);}
  .nw .thesis h2{font-size:clamp(34px,5.2vw,70px);color:var(--ink);max-width:16ch;} .nw .thesis h2 em{font-style:normal;color:var(--orange);}
  .nw .fee{color:#fff;position:relative;background:var(--dark) url(IMGtable.webp) center 35%/cover no-repeat;}
  .nw .fee::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,13,13,.9) 0%,rgba(15,13,13,.78) 50%,rgba(15,13,13,.86) 100%);}
  .nw .fee::after{content:"";position:absolute;left:0;top:0;width:100%;height:6px;background:var(--orange);}
  .nw .fee .wrap{position:relative;z-index:1;} .nw .fee .eye{color:var(--orange);}
  .nw .fee h2{font-size:clamp(36px,5.6vw,76px);color:#fff;max-width:15ch;margin-top:18px;} .nw .fee h2 em{font-style:normal;color:var(--orange);}
  .nw .fee .body{color:rgba(255,255,255,.82);margin-top:28px;} .nw .fee .body b{color:#fff;}
  .nw .fee .quote{margin-top:38px;display:grid;grid-template-columns:76px 1fr;gap:20px;align-items:start;border-left:5px solid var(--orange);padding-left:22px;}
  .nw .fee .quote img{width:76px;height:76px;border-radius:50%;object-fit:cover;display:block;border:2px solid rgba(255,255,255,.15);}
  .nw .fee .quote .k{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:clamp(26px,3.2vw,40px);text-transform:uppercase;line-height:1;color:var(--orange);}
  .nw .fee .quote .who{margin-top:10px;font-family:'Barlow',sans-serif;font-size:12.5px;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.6);}
  @media(max-width:520px){.nw .fee .quote{grid-template-columns:1fr;}}
  .nw .now{background:var(--paper);} .nw .now h2{font-size:clamp(36px,5.6vw,76px);color:var(--ink);max-width:14ch;} .nw .now h2 em{font-style:normal;color:var(--orange);}
  .nw .three{margin-top:48px;display:grid;grid-template-columns:repeat(3,1fr);border-top:2px solid var(--ink);}
  .nw .three > div{padding:28px 26px 30px 0;border-right:1px solid var(--line);} .nw .three > div + div{padding-left:26px;} .nw .three > div:last-child{border-right:none;}
  .nw .three h3{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:clamp(24px,2.6vw,32px);text-transform:uppercase;line-height:1;color:var(--orange);}
  .nw .three p{margin-top:12px;color:var(--ink-2);font-size:16.5px;} .nw .now .close{margin-top:44px;}
  @media(max-width:760px){.nw .three{grid-template-columns:1fr;}.nw .three > div{border-right:none;border-bottom:1px solid var(--line);padding:24px 0;}.nw .three > div + div{padding-left:0;}}
""".replace('IMG',IMG)
HTML2 = r"""  <section class="thesis"><div class="wrap two">
    <div class="rv"><div class="eye">The thesis</div><h2 class="disp" style="margin-top:18px">Attention is a commodity. <em>Trust is the only true currency.</em></h2></div>
    <div class="rv"><p class="body">Every network sells you attention &mdash; a room full of people who might, one day, need what you do.</p><p class="body">Trust is what actually moves work between businesses, and trust doesn&rsquo;t come from a membership tier. It comes from showing up, being useful, and doing what you said.</p></div>
  </div></section>
  <section class="fee"><div class="wrap two">
    <div class="rv"><div class="eye">What the fee does to people</div><h2 class="disp">A monthly fee turns curiosity into obligation. <em>And obligation is what people fake.</em></h2></div>
    <div class="rv">
      <p class="body">We ran a paid membership network for years. <b>It worked.</b> Real introductions, real deals, real partnerships.</p>
      <p class="body">And underneath it, slowly, the thing that makes people collaborate &mdash; genuine interest in each other &mdash; wore down into a calendar entry. Attendance became a chore. Conversations became transactions. The fee that was supposed to signal commitment ended up manufacturing the opposite.</p>
      <div class="quote"><img src="IMGchris.webp" alt="Chris White" width="640" height="640" loading="lazy"><div><div class="k">It got tedious.<br>So we did away with it.</div><div class="who">Chris White &middot; NOW Group</div></div></div>
    </div>
  </div></section>
  <section class="now"><div class="wrap">
    <div class="rv"><div class="eye">What NOW is now</div><h2 class="disp" style="margin-top:18px">An open meeting. <em>That&rsquo;s the whole product.</em></h2></div>
    <div class="three rv">
      <div><h3>Pay $50, once</h3><p>Not a month. Not a year that renews. Once.</p></div>
      <div><h3>Go through NET_SYNC</h3><p>Ten minutes, automated. We read what you do and who you need to meet, so your first meeting isn&rsquo;t a cold room.</p></div>
      <div><h3>Get your link</h3><p>One Zoom link. It doesn&rsquo;t change. You&rsquo;re in for twelve months.</p></div>
    </div>
    <p class="body close rv">No tiers. No &ldquo;upgrade to unlock introductions.&rdquo; Nothing to keep paying for. <b>If you get value, you&rsquo;ll come back.</b> If you don&rsquo;t, you&rsquo;re out $50 and an hour &mdash; and we&rsquo;d rather that than a year of you resenting a direct debit.</p>
  </div></section>
""".replace('IMG',IMG)
JS2 = "(function(){\n"+FINDROOT+REVEAL+"})();"

CSS3 = io.open('css3.txt',encoding='utf-8').read()
def star(): return '&#9733;'*5
screens=''.join("""          <div class="screen" data-i="%d"><div class="glass">
            <div class="top"><span class="stars">%s</span><span class="src">%s &middot; %s</span></div>
            <p class="q">&ldquo;%s&rdquo;</p>
            <div class="who"><b>%s</b><span>%s</span></div>
          </div></div>
""" % (i, star(), 'Google review' if t['source']=='Google' else 'LinkedIn', H.escape(t['date'].split('·')[0].strip()), H.escape(t['quote']), H.escape(t['name']), H.escape(t['role'])) for i,t in enumerate(T))
HTML3 = io.open('html3.txt',encoding='utf-8').read().replace('{{SCREENS}}',screens).replace('IMG',IMG)
JS3 = "(function(){\n"+FINDROOT+REVEAL+io.open('js3.txt',encoding='utf-8').read()+"\n})();"

def block(css, html, js, note):
    return ('<!-- NOW Group home · %s — one GHL Custom Code element, full-width section, padding 0 -->\n' % note
            + OVERRIDE + '<link rel="stylesheet" href="%s">\n' % FONT + JSHEAD
            + '<style>' + BASE + css + '</style>\n<div class="nw">\n' + html + '</div>\n<script>\n' + js + '\n</script>\n')
io.open('ghl/block-1-hero.html','w',encoding='utf-8').write(block(CSS1,HTML1,JS1,'BLOCK 1 · hero'))
io.open('ghl/block-2-argument.html','w',encoding='utf-8').write(block(CSS2,HTML2,JS2,'BLOCK 2 · the argument'))
io.open('ghl/block-3-console.html','w',encoding='utf-8').write(block(CSS3,HTML3,JS3,'BLOCK 3 · the console + close'))
io.open('ghl/home-ghl.html','w',encoding='utf-8').write(block(CSS1+CSS2+CSS3, HTML1+HTML2+HTML3, JS1+'\n'+JS2+'\n'+JS3, 'ALL IN ONE'))
standalone=('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>NOW Group — the open meeting</title><meta name="theme-color" content="#F03808"><link rel="stylesheet" href="%s"><style>body{margin:0;background:#F5F5F7}%s</style></head><body>\n' % (FONT, BASE+CSS1+CSS2+CSS3)
  + JSHEAD + '<div class="nw">\n'+HTML1+'</div>\n<script>\n'+JS1+'\n</script>\n<div class="nw">\n'+HTML2+'</div>\n<script>\n'+JS2+'\n</script>\n<div class="nw">\n'+HTML3+'</div>\n<script>\n'+JS3+'\n</script>\n</body></html>')
io.open('home.html','w',encoding='utf-8').write(standalone)
open('/tmp/nw3.js','w').write(JS1+'\n'+JS2+'\n'+JS3)
for f in ['ghl/block-1-hero.html','ghl/block-2-argument.html','ghl/block-3-console.html','ghl/home-ghl.html','home.html']: print('%-28s %6d' % (f, os.path.getsize(f)))
