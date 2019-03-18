#!/usr/bin/python

import gmpy
import binascii
from pwn import *

r = connect('2018shell2.picoctf.com', 36859)

def stage1():
	print r.recvuntil(':')
	r.sendline('y')
	print r.recvuntil('n:')
	p = 93187
	q = 94603
	n = p*q
	r.sendline(str(n))
	#8815769761

def stage2():
	print r.recvuntil(':')
	r.sendline('y')
	print r.recvuntil('q:')
	p = 81203
	n = 6315400919
	q = n/p
	r.sendline(str(q))
	#77773

def stage3():
	print r.recvuntil(':')
	r.sendline('n')
	#n

def stage4():
	print r.recvuntil(':')
	r.sendline('y')
	print r.recvuntil(':')
	q = 78203
	p = 79999
	phi = (p-1)*(q-1)
	r.sendline(str(phi))
	#6256003596

def stage5():
	print r.recvuntil(':')
	r.sendline('y')
	print r.recvuntil(':')
	m = 1815907181716474805136452061793917684000871911998851410864797078911161933431337632774829806207517001958179617856720738101327521552576351369691667910371502971480153619360010341709624631317220940851114914911751279825748
	e = 3
	n = 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331
	c = m**e % n 
	r.sendline(str(c))
	#26722917505435451150596710555980625220524134812001687080485341361511207096550823814926607028717403343344600191255790864873639087129323153797404989216681535785492257030896045464472300400447688001563694767148451912130180323038978568872458130612657140514751874493071944456290959151981399532582347021031424096175747508579453024891862161356081561032045394147561900547733602483979861042957169820579569242714893461713308057915755735700329990893197650028440038700231719057433874201113850357283873424698585951160069976869223244147124759020366717935504226979456299659682165757462057188430539271285705680101066120475874786208053

def stage6():
	print r.recvuntil(':')
	r.sendline('n')
	#n
	
def stage7():
	print r.recvuntil(':')
	r.sendline('y')
	print r.recvuntil(':')
	q = 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559
	p = 97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637
	e = 65537
	n = p*q
	phi = (p-1)*(q-1) 
	d = gmpy.invert(e, phi)
	r.sendline(str(d))
	#1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729

def stage8():
	print r.recvuntil(':')
	r.sendline('y')
	print r.recvuntil(':')
	p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
	q = 156408916769576372285319235535320446340733908943564048157238512311891352879208957302116527435165097143521156600690562005797819820759620198602417583539668686152735534648541252847927334505648478214810780526425005943955838623325525300844493280040860604499838598837599791480284496210333200247148213274376422459183
	c = 1191791154385603989017338950457953706444549348977257175840859024439456896961914986634158747079098646147275076768073561042920214249993651808989837779063107922958105481379936383065215869487850820431171263674544580096729254472650575604484973219990255615863148106543105096126096999191988960394375673790215786843107073528379091019699671260953369425507741892996006226548525831549275670809621483441808393283624850199270699755906043632045064848258791734958759503417667092878170518427857289905497710627257839284785457619198191563756900049939096535179455095450168682853409392860360775357790031928613703963238835882564864599021
	e = 65537
	n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
	phi = (p-1)*(q-1) 
	d = gmpy.invert(e, phi)
	m = pow(c, d, n)
	r.sendline(str(m))
	message  =  hex(m).split('x')[-1]
	print "Decrypt : " , binascii.unhexlify(message)
	#240109877286251840533272915662757983981706320845661471802585807564915966910384375649897669765182077

if __name__ == "__main__":
	stage1()
	stage2()
	stage3()
	stage4()
	stage5()
	stage6()
	stage7()
	stage8()
