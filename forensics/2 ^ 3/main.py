from math import gcd

# Given data
e = 65537
n = 19290563578327453949336521542006226917305579089238611319340418865328530239156980001148287094794597245123342342649855430461737481257157770687174830619431639754196595918514001386358652631605986698185365603862366462464354475435147445345755769464304858043419123264809730783029021355227182841798894442177927483078138507520231852246431337982584453172947670828725583176749755687698515274495507626279949858815116849415334900660204540013242983358025753756615290790683594556065352249470422727993888306130121329010803896204476837596104298196365868904948872583257714213914727558162469953472832667212915079478881070361647287015227

past_keys = [
    13634682244062493209535317287378641081468326517990274037123601085280572670602789584069432503759192981382751243322868632173207382308590505381868038691157029751197947611801438815439114317669390894439347417597015575948420494845824231713994873429669784068959172248647315244747955126515471501639261048607673430977766353168360899715115780670497208055271229956880676434385766427005244661461855609455012007039926208637486473683227550907779840335176305454862375732557792415469369471661608287326466460118968875765493925387466496814365453679408574167815228475613140811278611202066288944857617091672801857028333449173119090670241,
    19964983837564150411024495992270143343224352835765057169734081076642228813263457569979190650544193340800914243895854826087042162594251886725077648132556794214095210616197588600689459909397443955414906889667005526739156243943887882781573083921998413193662975688733113932627755513195805172201497582240513596364290634349906060658866718923795368935780413653309419014141004476669883952732392648498562596039131382791810185375707845850249814127135949467737591865028026966541459883627209958073475584455015064316444973758618819007991258073933750412418042479738466906231572923008071170517817535197651740906934300866642107858183,
    18889328381404668239720333947934830952021287651171901575256780880957068941326169892438524902705323260024732507400785222437913768639831014130872371288804587698332704684945760140233969917670052662471487155905274264197390617304032853073323543688429426122827473518872905186161574080142082855758748090023203653452274240008963436004027250568814023242041198685790935928653673399787054550871277508263662299871520040773994372406037802234852215009154861027306663029970599897806038582201601532772836238680370150414651420748241644520345132782909147139356403587754710180919137863113442282833804581007490529700367619118954135063751,
    12598389218740140579461608819512259513494605530748067612747825041616399381371807275747788343676681827239129433183632854227258697902285389930557767211969915989365183211420094806198856586018451759054123658471825060684141242370427695601995025226952809136986945616367486926003025108426533321358047129662997374286849027344721760207827550569131538156348063634204970341941721792781117086842691532456624308207594602626519584284663525182283083320102637173307906191855337992766432770113156372011280132124377352928426642537421627761138020904862611170348392774549500150425632747028586581326021622542058437652720468860629584865747,
    21009597895151991048957080170283815124260757619871599890323047085691338521114639475957087372180979723455575973768756433127965625839418928424865102814917604858107149143481117676395343080670586313482525295203828634102336673836504691701388647757453892313580600773332992094821357730728999381704688704666334340399942407837274583499050227490215885234348128507862215747188343522345736299034937455315236979763696197340211938298583511610123018063947628267553768524953595022011707343968101085316695416036590429502054422942272546535501327183872646581209806652969987269459577425816345309038852843425590500841893635274497284827263,
    15999189908967656407582517571287084079009874307412533585119810690472438620033611891212412301627441390518011580994873792338143422990125462384771294364773044005227846516389333140902823783545969640857193819114190931009861387456890668412818563889963198398406417699016221797984824021001367209338803575158636154621239690229908324761944294705169498519999617206289087244067197435156019292801546344393188500044301101889597577852797505222180244585145034689731841704995220902355407546203905607669145834523415106875959579712857719202326213910720529818449678642037147838398385835679292883721803482069360902175587332741595723208527,
    17060829917540070745030292243781553638590091899314190818159250455963505841792701295664796094574203198946132858945447916932084920280787094725952480768608869535012148171388285709119561558761672707862399888726042737101412487275888833989686715122957022437075714404243904633807300584831564725389538820125109408622298767397251766024535550323254342021712647181920368561517170975255002314338951076619020485429628802221772135646119959249072928741459990628737363931494652192292886508297052373778394814517125324281588928316855934631980781369461739044251458178241544679774280264290527571769804410623822046481731374693508172372433,
    14738513653498871549706819441346801177681246497723103663948270875796195110701206104587855600472107987592027677090098796239789666192874576939786629214894902983817232924925377203463734157036494332795840259905108129790769097897120533647954453217977363060830807541201842623609324654140547233879195533112035980256914768006116354187956163751273193869929239348303807265085534061539453683307581456336166630229280475960695656193373161574640186013831556530259722906801185586577884403226762727312395475054559080821971932963060901989676999431551821286226026673473225602684580072913417554771318259964900830081247371572868207317703,
    18286405907934052226952046558180358257132137807342087990642195125902901347015767746217962913187157765450575178004580338595787658186086828103650848031067019548430317554317532155902277266893473765238972821710205429510303271429851717543179620013622720935258534698063616461069254822435315713510034206051306435695294352957309546770853848980015534041585461499082441214678038815962482833001461225568481090673110402278246867487864633176526859926494463634917147485681085143328702519961588713293247646453108381251417120898674843582541191156516387817503009654497920230002218581920538258572965874552929213065954817686800766402461,
    111109379347255653345252877622529896969961448626515153952065702925165019258913883757664119227251508705457635528020074963699346126839707142189761315066220597545569627437679169565906013931408004717717657763016662333276580794120049447441906186600256371016054178914907212486267583982914008379220590003676445157178773268861198868995610021237344083896199826161321816696006788755036399036250768357325111273643210926013461174430764175138729470518698156750892291732722154586419321866274919388488443933115188932775563516997243865346112199481075271268378278930516184559858867227866956260033866470322508710935995805194855125539360149
]

# Find gcd between e and each past_key's e
for i, past_e in enumerate(past_keys):
    common_factor = gcd(e, past_e)
    if common_factor != 1:
        print(f"Common factor found between e and past_keys[{i}]: {common_factor}")
