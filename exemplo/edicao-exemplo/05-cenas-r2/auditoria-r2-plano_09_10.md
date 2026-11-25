# Auditoria 2ª rodada · plano_09_10 (q412–q579, trechos 9 e 10)
*2026-11-20 · agente da cena · briefing `motor/briefing-cena-r2.md`*

## 1 · Refs lidas e o que medem de câmera
- **V04-A45** (trecho 9, parede). Câmera (reestudo 20/11, de 4 em 4 quadros): f3381 −7,6 %/s · f3392 −31,5 · f3404 −33,3 ·
  f3416 −34,0 (pico) · f3428 −21,7 · f3436 −13,6; corta ainda a −13 %/s. Fase única: recuo que acelera e freia. Ref f3386
  (início da aceleração, +5 ms do número) = nosso "todos" (i70) + 5 ms. Sem giro, sem borrão, 24 imagens/s.
  Acabamento da Ref: folhas sem moldura e sem sombra, "luz de museu" própria da cena.
- **V01-A38** (trecho 10, peça que cai por cima). Estalo de queda em degraus de 2 q (mantido). Câmera: a pilha sobe e recua
  devagar: −1,3 %/s e 0,41 px/q (720) com a 1ª foto; −2,4 %/s e 1,86 px/q com a 2ª; a cena de trás segue com a câmera dela.
- Painel (`03-plano/escolhas-r2.md`): trecho 9 "Recuo que acelera em 'todos' (−30 %/s) e freia; retoma +3 %/s em 'prontos'";
  trecho 10 "Repouso de +3 %/s; quase para enquanto os adesivos caem em 'PowerPoint' e 'Google Slides'; o fundo escurece."

## 2 · Tabela da câmera (taxa que sai da função = 100·ln(z(t+1q)/z(t))/1q)
Zoom relativo ao cartão de 858 px. 1º quadro q412: **1,054** (igual ao corte 03). Último q578: **0,585** (corte 03: ≈ 0,447).

| fase | intervalo | taxa pedida | taxa medida na função |
|---|---|---|---|
| pré-recuo (Ref) | q412–q428 | −7,6 %/s | −7,6 (q412…q424) |
| acelera em "todos" (Ref) | q428 → q434 (+250 ms) | −7,6 → −31,5 | −9,6 (q428) · −25,5 (q432) · −31,9 (q436) |
| pico (Ref) | q440–q460 | −33,3 → −34,0 | −32,5 · −33,1 · −33,4 · −33,6 · **−33,9 em q456** · −32,5 (q460) |
| freio (Ref) | q460 → q478 | −34,0 → −21,7 → −13,6 | −27,9 (q464) · −19,1 (q472) · −15,1 (q476) |
| freio até parar (nosso, desaceleração da Ref ≈ 30 %/s²) | q478 → q489 | −13,6 → 0 em "prontos"+135 ms | −10,6 (q480) · −5,7 (q484) · −0,9 (q488) |
| retoma (painel) | q489 → q495 | 0 → +3 | +1,6 (q492) · +3,0 (q496) |
| repouso (painel) | q495–q537 | +3 | +3,0 |
| quase para nos adesivos (painel) | q543 → q566 (rampas de 250 ms) | +0,3 | +1,4 (q540) · +0,3 (q544…q564) · +1,4 (q568) |
| retoma e corta andando | q572–q578 | +3 | +3,0 |

- Pico do recuo: **q456–q459, −33,9 %/s**, logo no início de "Depois," (19.160 ms); a aceleração começa em "todos" (+5 ms).
- Pilha (menu + 2 adesivos, peças presas à tela, âncora no centro do menu): parada até o menu assentar (q521); depois
  −1,3 %/s e sobe 0,6 px/q; depois do 2º adesivo assentar (q566), −2,4 %/s e 2,8 px/q. No q578: ×0,964, 61 px acima.

## 3 · O que mudou de acabamento
- `base.cena(..., semente=910)`: mesa do perfil V03 parada, grão vivo sobre as peças.
- **Saiu a "luz de museu"** (`c.vinheta = luz_museu(...)`, herdada da V04-A45): nenhuma vinheta por cima das peças.
- 60 cartões da parede e o cartão do menu: `pecas.cartao` agora devolve o cartão do perfil (borda de papel pontilhada de
  12 px em vez de 11, fio escuro, sombra caída incluída). Nenhum posicionamento usa o tamanho do RGBA: a margem nova não
  desloca nada.
- Logos: `pecas.recorte` → `pecas.recorte_do_perfil` (contorno branco ondulado + sombra do perfil). Sombra do adesivo
  sobre o menu aparece (peça sobre peça clara: o certo).
- **Véu do trecho 10 (pedido do Felipe) mantido igual:** `VEU = 0.62`, 2 degraus de 2 q em "PowerPoint" (q543), entre a cena
  e os adesivos. Ficou sem `sem_grao`, para o grão da parede escurecida cair na proporção certa.

## 4 · O que ficou igual
- Cortes q412–q579, ordem e gatilhos. `eventos` antes e depois (impresso pelos dois perfis):
  `{'corte_entrada': 412, 'acelera': 428, 'cartao_ppt': 517, 'logo_powerpoint': 543, 'logo_google_slides': 562, 'corte_saida': 579}`: idêntico.
  (O plano devolve `eventos`, não `gatilhos`; a chave não foi trocada.)
- Composição: grade 5×12, passos, desalinhamentos, giros, rodízio de slides, ponto fixo (540, 864), menu 991 px em
  (546, 580) com +1,4°, logos em (330, 905) e (735, 930), 300 px, giros −6° e +5°, estalos.
- Comparação de folhas (corte 03 × r2, q412–q579 passo 4): mesma composição e mesmos tempos de entrada.

## 5 · Painel × Ref
- Pico do recuo: painel −30 %/s, Ref −34 %/s → **vale a Ref** (−33,9 na função).
- A Ref corta a −13 %/s; a nossa cena não corta: o resto (parar e retomar +3 %/s em "prontos") veio do painel.
- Trecho 10: a V01-A38 mede o movimento da PILHA (recua e sobe), o painel fala da câmera da cena (+3 %/s, quase para).
  Não se contradizem: a parede segue o painel; o menu e os adesivos seguem a pilha da Ref.
- Divergência da spec antiga: a spec do corte 03 usava uma tabela de larguras com pico ≈ −40 %/s e terminava ×0,454; a
  câmera do reestudo (−34) recua menos: no fim a parede está ≈ 29 % maior (menos cartões à vista, ≈ 3 colunas e 6–7 linhas).
  Continua sangrando as 4 bordas em todos os quadros.
- Acabamento: a V04-A45 diz "folhas sem moldura e sem sombra"; o perfil V03 manda borda e sombra. Seguido o perfil (como o
  briefing manda). A sombra cai nos vãos escuros e quase some; fica visível como um vão um pouco mais escuro embaixo de cada slide.

## 6 · Quadro seguro e leitura
- q484 (fim do freio) e q578 (último): parede sangra as 4 bordas; menu inteiro na tela (topo ≈ y 210 no q578), as linhas
  "PowerPoint (.pptx)" legíveis mesmo sob o véu; os dois adesivos inteiros; legenda legível sobre a tarja.
- Nada sai da tela antes de dar para ler: a câmera só recua (revela) no trecho 9 e quase não anda no trecho 10.

## 7 · Tempo de render
Por quadro (3 repetições, mesma máquina, pela trava): corte 03 34 / 38 / 45 / 63 ms (q420 / q470 / q530 / q570); r2
52 / 61 / 66 / 88 ms. ≈ 1,4–1,6× mais lento (o grão vivo de tela inteira), pico de memória 0,60 GB. Não é um problema.

## 8 · O que não consegui conferir
- Não vi o movimento em vídeo (só folhas e quadros); a inversão recuo → aproximação em "prontos" precisa ser vista andando.
- Não medi a sombra dos cartões da parede em pixel; só observei na folha.
- Folhas: `scratchpad/e3-r2/plano_09_10/` (c03-folha.jpg, r2-folha.jpg, r2-pico.jpg, r2-adesivos.jpg, r2-q578.png, r2-q484.png).
