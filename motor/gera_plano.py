#!/usr/bin/env python3
"""gera_plano.py · Estilo 03 · monta o plano de edição em HTML (seção 6 do CLAUDE.md do projeto).

Uso: python3 gera_plano.py <pasta 03-plano>      (lê beats.json, grava plano-de-edicao.html)

A miniatura de cada opção é o thumb.jpg da referência (skill: biblioteca/<ID …>/thumb.jpg): mostra só a FORMA.
A descrição diz com que conteúdo do tema do vídeo cada lacuna será preenchida.

Regras do painel (autor do método): toda edição passa por ele; todo trecho tem SEMPRE três opções, e uma delas leva
a minha recomendação ("Minha sugestão"). No topo fica o perfil de acabamento (padrão V03), que ele pode trocar por vídeo.
O gerador recusa um beats.json que não tenha 3 opções e 1 sugestão em cada trecho.
"""
import os, sys, json, glob, html
from urllib.parse import quote

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import perfis
BIB = os.path.normpath(os.path.join(AQUI, '..', 'biblioteca'))
plano = os.path.abspath(sys.argv[1])
B = json.load(open(os.path.join(plano, 'beats.json'), encoding='utf-8'))

pasta = json.load(open(os.path.join(BIB, 'index.json'), encoding='utf-8'))   # id da Ref -> nome da pasta
import shutil
REFS = os.path.join(plano, 'refs')      # o painel é autossuficiente: miniaturas e notas usadas são copiadas para cá


def copia_ref(r):
    """Copia a miniatura e a nota da Ref `r` para <plano>/refs/ e devolve os caminhos relativos ao painel."""
    os.makedirs(REFS, exist_ok=True)
    thumb = os.path.join(BIB, pasta[r], 'thumb.jpg')          # pode não existir (miniaturas removidas): o painel segue sem a imagem
    if os.path.exists(thumb): shutil.copy(thumb, os.path.join(REFS, r + '.jpg'))
    nota = os.path.join(BIB, pasta[r], 'notes.md')
    if os.path.exists(nota): shutil.copy(nota, os.path.join(REFS, r + '.txt'))
    return ('refs/' + r + '.jpg' if os.path.exists(thumb) else ''), 'refs/' + r + '.txt'
falta = []
for b in B['beats']:
    for o in b['opcoes']:
        o['midia'] = []
        for r in o['refs']:
            if r not in pasta:
                falta.append(r); continue
            still, nota = copia_ref(r)
            o['midia'].append({'id': r, 'still': still, 'clip': '', 'nota': nota})
if falta: sys.exit('referência que não existe na biblioteca (confira o id em biblioteca/index.json): ' + ', '.join(falta))
ruins = [str(b['n']) for b in B['beats'] if len(b['opcoes']) != 3 or sum(1 for o in b['opcoes'] if o.get('sug')) != 1]
if ruins: sys.exit('todo trecho precisa de 3 opções e exatamente 1 sugestão; fora da regra: trechos ' + ', '.join(ruins))

# perfis de acabamento (motor/perfis.py): o padrão vem marcado; a miniatura mostra a cara de cada um na referência
B['perfil_padrao'] = B.get('perfil_padrao', perfis.PADRAO)
B['perfis'] = []
for k in perfis.ORDEM:
    P = perfis.PERFIS[k]
    midia = []
    for r in P['refs']:
        if r in pasta:
            still, nota = copia_ref(r)
            midia.append({'id': r, 'still': still, 'clip': '', 'nota': nota})
    B['perfis'].append({'k': k, 'nome': P['nome'], 'resumo': P['resumo'], 'pontos': P['pontos'], 'midia': midia})

CHAVE = 'e3-plano-' + os.path.basename(os.path.dirname(plano)) + ('-r' + str(B['rodada']) if B.get('rodada') else '')   # rodada nova = escolhas limpas
CSS = """
:root{--bg:#131312;--card:#1c1c1a;--line:#2e2d2a;--tx:#ecebe6;--mut:#a09d94;--rosto:#8a877f;--over:#9cc7e6;--cena:#3f8fd0;--ok:#e8c84a}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
main{max-width:1280px;margin:0 auto;padding:28px 24px 80px}
h1{font-size:26px;margin:0 0 4px;font-weight:650}h1 span{color:var(--mut);font-weight:400}
.meta{color:var(--mut);font-size:13.5px;margin:2px 0}.meta b{color:var(--tx);font-weight:550}
.top{display:flex;gap:16px;align-items:flex-start;justify-content:space-between;flex-wrap:wrap}
.acoes{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.selo{font-size:12.5px;color:var(--mut);border:1px solid var(--line);border-radius:99px;padding:5px 11px}
button{font:inherit;cursor:pointer;border-radius:8px;border:1px solid var(--line);background:#26251f;color:var(--tx);padding:8px 14px}
button:hover{border-color:#55524a}button.pri{background:var(--ok);color:#1a1808;border-color:var(--ok);font-weight:600}
.painel{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:18px 0}
.tl{display:flex;height:46px;border-radius:8px;overflow:hidden;background:#0d0d0c}
.tl a{display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:600;color:#10100e;text-decoration:none;border-right:2px solid var(--bg);min-width:0}
.tl a.rosto{background:var(--rosto)}.tl a.overlay{background:var(--over)}.tl a.cena{background:var(--cena);color:#fff}
.tl a.pend{opacity:.45}
.regua{display:flex;justify-content:space-between;color:var(--mut);font-size:11.5px;margin-top:5px}
.leg{display:flex;gap:16px;flex-wrap:wrap;color:var(--mut);font-size:12.5px;margin-top:10px}.leg i{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px;margin-top:14px}
.num{border:1px solid var(--line);border-radius:10px;padding:10px 12px}.num b{font-size:21px;font-weight:650;display:block}
.num small{color:var(--mut);font-size:12.5px}.num.fora b{color:#f0a35c}.num.dentro b{color:#9bd08a}
.beat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px;margin:16px 0;scroll-margin-top:12px}
.bh{display:flex;justify-content:space-between;gap:12px;align-items:baseline;flex-wrap:wrap;margin-bottom:10px}
.bh h2{font-size:18px;margin:0}.bh h2 span{color:var(--mut);font-weight:400;font-size:14px;margin-left:8px}
.esc{font-size:13px;color:var(--ok)}
.grade{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:18px}
@media(max-width:980px){.grade{grid-template-columns:1fr}}
textarea{width:100%;min-height:54px;background:#121211;color:var(--tx);border:1px solid var(--line);border-radius:8px;padding:9px 11px;font:inherit;resize:vertical}
.ops{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:12px}
@media(max-width:760px){.ops{grid-template-columns:1fr}}
.op{border:1px solid var(--line);border-radius:10px;padding:10px;display:flex;flex-direction:column;gap:8px;background:#181816}
.op.on{border-color:var(--ok);box-shadow:0 0 0 1px var(--ok) inset}
.thumbs{display:flex;gap:8px;justify-content:center;background:#101010;border-radius:8px;padding:8px}.thumbs button{padding:0;border:0;background:#000;border-radius:6px;overflow:hidden;flex:0 0 auto;position:relative;height:270px;aspect-ratio:9/16}
.thumbs img{width:100%;height:100%;object-fit:cover;display:block}.thumbs span{position:absolute;left:5px;bottom:5px;background:rgba(0,0,0,.72);color:#fff;font-size:10.5px;padding:1px 6px;border-radius:4px}
.semref{height:286px;border:1px dashed var(--line);border-radius:6px;display:flex;align-items:center;justify-content:center;color:var(--mut);font-size:12.5px;text-align:center;padding:10px}
.op h3{font-size:14.5px;margin:0;line-height:1.3}.op h3 b{color:var(--mut);margin-right:5px}
.cat{font-size:12px;color:var(--mut)}.desc{font-size:13.2px;color:#d6d4cc}.ref{font-size:12px;color:var(--mut)}.ref a{color:var(--over)}
.sug{align-self:flex-start;font-size:11px;font-weight:650;background:#3a3312;color:var(--ok);border-radius:99px;padding:2px 9px}
.op .usar{margin-top:auto}.op.on .usar{background:var(--ok);color:#1a1808;border-color:var(--ok);font-weight:600}
.lado h4{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--mut);margin:0 0 5px}
.lado p{margin:0 0 14px;font-size:14px}.lado .visto{font-size:13px;color:#cfcdc5}
.lado video{width:100%;max-width:220px;border-radius:8px;background:#000;display:block;margin-bottom:14px}
details{margin-top:8px}summary{cursor:pointer;color:var(--mut)}details li{margin:4px 0;font-size:13.5px}
dialog{border:0;border-radius:12px;background:#000;padding:0;max-width:92vw}dialog::backdrop{background:rgba(0,0,0,.8)}
dialog video{display:block;max-height:86vh;max-width:92vw}dialog form{position:absolute;right:8px;top:8px}
.aviso{color:var(--mut);font-size:13px;margin-top:10px}
.painel h2{font-size:17px;margin:0 0 4px}.painel .sub{color:var(--mut);font-size:13.5px;margin:0 0 12px;max-width:92ch}
.perfis{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media(max-width:860px){.perfis{grid-template-columns:1fr}}
.pf{border:1px solid var(--line);border-radius:10px;padding:10px;background:#181816;display:flex;flex-direction:column;gap:8px}
.pf.on{border-color:var(--ok);box-shadow:0 0 0 1px var(--ok) inset}
.pf h3{font-size:14.5px;margin:0}.pf ul{margin:0;padding-left:17px;font-size:12.8px;color:#d6d4cc}.pf li{margin:3px 0}
.pf .thumbs button{height:200px}.pf .usarpf{margin-top:auto}.pf.on .usarpf{background:var(--ok);color:#1a1808;border-color:var(--ok);font-weight:600}
.cam{font-size:12.6px;color:#c9dcec;border-left:2px solid #3f8fd0;padding-left:8px}.cam b{color:var(--over);font-weight:600}
.notasug{font-size:12.5px;color:var(--ok);margin:0 0 8px}
"""
JS = r"""
const D=__DADOS__, CH=__CHAVE__;
let S={}; try{S=JSON.parse(localStorage.getItem(CH)||'{}')}catch(e){}
const salva=()=>{try{localStorage.setItem(CH,JSON.stringify(S))}catch(e){}};
const fmt=ms=>(ms/1000).toFixed(2).replace('.',',')+' s';
const op=(b,k)=>b.opcoes.find(o=>o.k===k);
const vigente=b=>{const e=S[b.n]&&S[b.n].k;return e?op(b,e):b.opcoes.find(o=>o.sug)};
const perfilVig=()=>S._perfil||D.perfil_padrao;
function desenhaPerfis(){document.querySelectorAll('.pf').forEach(el=>{const on=el.dataset.k===perfilVig();el.classList.toggle('on',on);
  el.querySelector('.usarpf').textContent=on?(S._perfil?'Escolhido':'Marcado (padrão)'):'Usar este perfil';});
  const p=D.perfis.find(x=>x.k===perfilVig());document.getElementById('pfvig').textContent=p.nome+(S._perfil?'':' (padrão, ainda não confirmado)');}
function contas(){
  let ant=null,rosto=0,cortes=0;
  D.beats.forEach((b,i)=>{const o=vigente(b);let ef=o.tipo==='segue'?(ant||'cena'):(o.tipo==='cena'?'cena':'rosto');
    if(i>0&&o.tipo!=='segue'){ if(ef!==ant) cortes++; else if(ef==='cena'&&o.entrada==='corte') cortes++; }
    if(ef==='rosto') rosto+=b.fim-b.ini; b._ef=ef; ant=ef;});
  return {rosto,cortes};
}
function desenha(){
  const c=contas(), dur=D.duracao_ms, pal=D.beats.reduce((s,b)=>s+b.fala.trim().split(/\s+/).length,0);
  const tl=document.getElementById('tl'); tl.innerHTML='';
  D.beats.forEach(b=>{const o=vigente(b),e=S[b.n]&&S[b.n].k;const a=document.createElement('a');a.href='#b'+b.n;a.textContent=b.n;
    const cor=o.tipo==='overlay'?'overlay':(b._ef==='rosto'?'rosto':'cena');a.className=cor+(e?'':' pend');a.style.flex=(b.fim-b.ini)+' 0 0';
    a.title='Trecho '+b.n+' · '+fmt(b.ini)+' a '+fmt(b.fim)+' · '+o.nome+(e?'':' (sugestão, ainda não escolhido)');tl.appendChild(a);});
  const pr=100*c.rosto/dur, c10=c.cortes/(dur/10000), c100=100*c.cortes/pal, esc=D.beats.filter(b=>S[b.n]&&S[b.n].k).length;
  const cls=(v,a,b)=>'num '+(v>=a&&v<=b?'dentro':'fora');
  document.getElementById('nums').innerHTML=
   `<div class="num"><b>${esc} de ${D.beats.length}</b><small>trechos escolhidos (os outros contam pela sugestão)</small></div>`+
   `<div class="${cls(pr,D.referencia.rosto_pct[0],D.referencia.rosto_pct[1])}"><b>${pr.toFixed(1).replace('.',',')} %</b><small>do tempo no rosto · referência: 14 a 21 %</small></div>`+
   `<div class="${cls(c10,D.referencia.cortes_10s[0],D.referencia.cortes_10s[1])}"><b>${c10.toFixed(1).replace('.',',')}</b><small>cortes secos por 10 s · referência: 2,1 a 2,6</small></div>`+
   `<div class="${cls(c100,6.3,7.9)}"><b>${c100.toFixed(1).replace('.',',')}</b><small>cortes por 100 palavras · referência: 6,3 a 7,9 (você fala mais rápido)</small></div>`;
  D.beats.forEach(b=>{const e=S[b.n]&&S[b.n].k;document.getElementById('esc'+b.n).textContent=e?'Escolhido: '+e+' · '+op(b,e).nome:'';
    b.opcoes.forEach(o=>{const el=document.getElementById('op'+b.n+o.k);el.classList.toggle('on',e===o.k);el.querySelector('.usar').textContent=e===o.k?'Escolhido':'Usar este';});});
}
function monta(){
  const root=document.getElementById('beats');
  D.beats.forEach(b=>{
    const s=document.createElement('section');s.className='beat';s.id='b'+b.n;
    s.innerHTML=`<div class="bh"><h2>Trecho ${b.n}<span>${fmt(b.ini)} a ${fmt(b.fim)} · ${fmt(b.fim-b.ini)} · ${b.tipo}</span></h2><div class="esc" id="esc${b.n}"></div></div>
    ${b.nota_sug?`<p class="notasug">${b.nota_sug}</p>`:''}
    <div class="grade"><div><textarea id="nt${b.n}" placeholder="Escreva seu plano para este trecho ou escolha um design abaixo e edite"></textarea>
    <div class="ops">${b.opcoes.map(o=>`<div class="op" id="op${b.n}${o.k}">
      ${o.midia.length?`<div class="thumbs">${o.midia.map(m=>`<button type="button" data-clip="${m.clip}" data-nota="${m.nota}" title="Ver a medida da referência ${m.id}"><img loading="lazy" src="${m.still}" alt="Referência ${m.id}"><span>${m.id}</span></button>`).join('')}</div>`:`<div class="semref">sem imagem nova:<br>a cena anterior continua</div>`}
      ${o.sug?'<span class="sug">Minha sugestão</span>':''}
      <h3><b>${o.k}</b>${o.nome}</h3><div class="cat">${o.cat} · entra por ${o.tipo==='segue'?'continuidade':(o.entrada==='corte'?'corte seco':'movimento, sem corte')}</div>
      <div class="desc">${o.desc}</div>
      ${o.camera?`<div class="cam"><b>Câmera:</b> ${o.camera}</div>`:''}
      <div class="ref">${o.midia.length?'Ref '+o.midia.map(m=>`<a href="${m.nota}" target="_blank">${m.id}</a>`).join(' + ')+' (a miniatura mostra só a forma)':'Sem referência de imagem'}</div>
      <button type="button" class="usar" data-b="${b.n}" data-k="${o.k}">Usar este</button></div>`).join('')}</div></div>
    <div class="lado"><h4>Roteiro</h4><p>“${b.fala}”</p><h4>Clipe neste trecho</h4>
      <video controls playsinline preload="metadata" data-ini="${b.ini/1000}" data-fim="${b.fim/1000}" src="${D.clipe}#t=${b.ini/1000},${b.fim/1000}"></video>
      <h4>Visto nos reels</h4><p class="visto">${b.visto}</p></div></div>`;
    root.appendChild(s);
    const t=s.querySelector('textarea');t.value=(S[b.n]&&S[b.n].nota)||'';
    t.addEventListener('input',()=>{S[b.n]=S[b.n]||{};S[b.n].nota=t.value;salva();});
  });
  const pr=document.getElementById('perfis');
  D.perfis.forEach(p=>{const d=document.createElement('div');d.className='pf';d.dataset.k=p.k;
    d.innerHTML=`<div class="thumbs">${p.midia.map(m=>`<button type="button" data-clip="${m.clip}" data-nota="${m.nota}" title="Ver a medida desta referência"><img loading="lazy" src="${m.still}" alt="Referência ${m.id}"><span>${m.id}</span></button>`).join('')}</div>
      ${p.k===D.perfil_padrao?'<span class="sug">Minha sugestão · padrão do estilo</span>':''}
      <h3>${p.nome}</h3><ul>${p.pontos.map(x=>`<li>${x}</li>`).join('')}</ul>
      <button type="button" class="usarpf">Usar este perfil</button>`;
    d.querySelector('.usarpf').addEventListener('click',()=>{S._perfil=p.k;salva();desenhaPerfis();});pr.appendChild(d);});
  document.querySelectorAll('.usar').forEach(bt=>bt.addEventListener('click',()=>{const n=bt.dataset.b,k=bt.dataset.k;S[n]=S[n]||{};S[n].k=(S[n].k===k?null:k);salva();desenha();}));
  document.querySelectorAll('.lado video').forEach(v=>{const a=+v.dataset.ini,f=+v.dataset.fim;
    v.addEventListener('play',()=>{if(v.currentTime<a-0.05||v.currentTime>=f-0.03)v.currentTime=a;});
    v.addEventListener('timeupdate',()=>{if(v.currentTime>=f){v.pause();v.currentTime=a;}});});
  const dlg=document.getElementById('dlg'),dv=dlg.querySelector('video');
  document.querySelectorAll('.thumbs button').forEach(bt=>bt.addEventListener('click',()=>{if(!bt.dataset.clip){if(bt.dataset.nota)window.open(bt.dataset.nota,'_blank');return;}dv.src=bt.dataset.clip;dlg.showModal();dv.play().catch(()=>{});}));
  dlg.addEventListener('close',()=>{dv.pause();dv.removeAttribute('src');dv.load();});
  dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close();});
  document.getElementById('todas').addEventListener('click',()=>{if(!S._perfil)S._perfil=D.perfil_padrao;desenhaPerfis();D.beats.forEach(b=>{S[b.n]=S[b.n]||{};if(!S[b.n].k)S[b.n].k=b.opcoes.find(o=>o.sug).k;});salva();desenha();});
  document.getElementById('limpa').addEventListener('click',()=>{if(confirm('Apagar todas as escolhas e anotações deste plano?')){S={};salva();document.querySelectorAll('textarea').forEach(t=>t.value='');desenha();desenhaPerfis();}});
  document.getElementById('copia').addEventListener('click',copia);
}
function texto(){
  const c=contas(),pf=D.perfis.find(x=>x.k===perfilVig());let t='PLANO DE EDIÇÃO · '+D.titulo+'\n'+D.estilo+'\nClipe: '+D.fonte+'\n';
  t+='Perfil de acabamento: '+pf.k+' · '+pf.nome+(S._perfil?'':' (padrão; não confirmei)')+'\n\n';
  D.beats.forEach(b=>{const e=S[b.n]&&S[b.n].k,o=e?op(b,e):null,nota=(S[b.n]&&S[b.n].nota||'').trim();
    t+='Trecho '+b.n+' · '+fmt(b.ini)+' a '+fmt(b.fim)+'\nFala: "'+b.fala+'"\n';
    t+=o?('Escolha: '+o.k+' · '+o.nome+' ('+o.cat+')\nRef: '+(o.refs.join(' + ')||'sem referência')+'\n'+(o.camera?'Câmera: '+o.camera+'\n':'')):'Escolha: NENHUMA (decida você ou siga a sugestão '+b.opcoes.find(x=>x.sug).k+')\n';
    t+='Observações: '+(nota||'nenhuma')+'\n\n';});
  t+='Contas com estas escolhas: rosto '+(100*c.rosto/D.duracao_ms).toFixed(1)+' % · '+c.cortes+' cortes secos ('+(c.cortes/(D.duracao_ms/10000)).toFixed(1)+' por 10 s)\n';
  return t;
}
function copia(){const t=texto(),bt=document.getElementById('copia');const ok=()=>{bt.textContent='Plano copiado';setTimeout(()=>bt.textContent='Copiar plano',1800)};
  const velho=()=>{const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy');ok()}catch(e){alert(t)}a.remove()};
  if(navigator.clipboard&&window.isSecureContext)navigator.clipboard.writeText(t).then(ok,velho);else velho();}
monta();desenha();desenhaPerfis();
"""
dados = json.dumps(B, ensure_ascii=False)
pagina = f"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Plano de edição · {html.escape(B['titulo'])}</title><style>{CSS}</style></head><body><main>
<div class="top"><div><h1>{html.escape(B['titulo'])} <span>· plano de edição</span></h1>
<p class="meta"><b>Clipe:</b> {html.escape(B['fonte'])}</p>
<p class="meta"><b>Duração:</b> {B['duracao_ms']/1000:.2f} s · {len(B['beats'])} trechos &nbsp; <b>Estilo:</b> {html.escape(B['estilo'])}</p></div>
<div class="acoes"><span class="selo">o plano salva sozinho neste navegador</span><button id="todas" type="button">Usar minhas sugestões no que falta</button><button id="limpa" type="button">Limpar</button><button id="copia" class="pri" type="button">Copiar plano</button></div></div>
<div class="painel"><h2>1 · Perfil de acabamento <span style="color:var(--mut);font-weight:400;font-size:13.5px">· vale para o vídeo inteiro · agora: <span id="pfvig"></span></span></h2>
<p class="sub">Luz da mesa, grão do papel, sombra, borda, cadência e a tarja da legenda vêm do mesmo reel de referência. O padrão vem marcado; você troca aqui, por vídeo. Dentro de um vídeo o perfil é um só. As miniaturas mostram a cara de cada perfil na referência (clique para abrir a medida do reel).</p>
<div class="perfis" id="perfis"></div></div>
<div class="painel"><h2>2 · Os trechos <span style="color:var(--mut);font-weight:400;font-size:13.5px">· três opções em cada um, com a minha sugestão marcada</span></h2><div class="tl" id="tl"></div><div class="regua">{''.join(f'<span>{s} s</span>' for s in range(0, int(B['duracao_ms']/1000) + 1, 5))}</div>
<div class="leg"><span><i style="background:var(--rosto)"></i>rosto + legenda</span><span><i style="background:var(--over)"></i>texto por cima do rosto</span><span><i style="background:var(--cena)"></i>cena de tela cheia</span><span>bloco apagado = ainda não escolhido (mostra a sugestão)</span></div>
<div class="nums" id="nums"></div>
<p class="aviso">Neste estilo a maior parte do vídeo é cena de tela cheia, e o rosto volta só nas viradas. As contas acima mudam conforme as suas escolhas. A legenda amarela em tarja (P01) fica no vídeo inteiro, menos nos planos de texto grande sobre o rosto.</p>
<details><summary>Como ler as opções</summary><ul>
<li>A miniatura é um quadro do reel de referência: mostra a <b>forma</b> (composição, tratamento, movimento). Clique para abrir a medida dessa referência. Nenhuma imagem da referência entra no seu vídeo.</li>
<li>A descrição diz com que <b>conteúdo do seu tema</b> cada lugar da forma será preenchido: prints reais do Claude, logos oficiais, documentos reais.</li>
<li>"[1 vídeo]" marca o que só existe em um dos 5 reels: é opção, não o padrão do estilo.</li>
<li>A linha <b>Câmera</b> de cada opção diz em que palavra cai o pico da aproximação e onde a câmera para. Na referência a câmera de cada cena tem fases amarradas à fala; não existe zoom igual do começo ao fim.</li>
<li>A legenda é uma tarja preta translúcida: some sobre a mesa escura, vira caixa escura sobre o rosto e retângulo cinza sobre papel claro. Nas opções de texto grande sobre o rosto, a legenda some naquele plano.</li>
<li>Quer algo diferente das três? Escreva na caixa do trecho.</li></ul></details></div>
<div id="beats"></div>
<dialog id="dlg"><form method="dialog"><button>Fechar</button></form><video controls playsinline></video></dialog>
</main><script>{JS.replace('__DADOS__', dados).replace('__CHAVE__', json.dumps(CHAVE))}</script></body></html>"""
dest = os.path.join(plano, 'plano-de-edicao.html')
open(dest, 'w', encoding='utf-8').write(pagina)
print(dest, len(pagina) // 1024, 'KB ·', len(B['beats']), 'trechos ·', sum(len(o['midia']) for b in B['beats'] for o in b['opcoes']), 'miniaturas')
