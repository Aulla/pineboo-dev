# -*- coding: utf-8 -*-
from pineboolib.qsa import *

#/** @file */

#/** @class_declaration interna */
class interna(object):
    ctx = Object()
    def __init__(self, context=None):
        self.ctx = context
    
    def init(self):
        self.ctx.interna_init()
    

#/** @class_declaration oficial */
class oficial(interna):
    iPaso = None
    aPasos = None
    formActual = None
    oMemoria = None
    oBucle = None
    oEventoEsperado = None
    aPilaForms = None
    fPaso = None
    log = None
    testing = None
    def __init__(self, context=None):
        super(oficial, self).__init__(context)
    
    def recibeEvento(self, tipo=None, emisor=None):
        return self.ctx.oficial_recibeEvento(tipo, emisor)
    
    def lanzaTest(self, fN=None):
        return self.ctx.oficial_lanzaTest(fN)
    
    def ejecutaPaso(self):
        return self.ctx.oficial_ejecutaPaso()
    
    def finTest(self, tipo=None):
        return self.ctx.oficial_finTest(tipo)
    
    def esperarEvento(self, oEvento=None):
        return self.ctx.oficial_esperarEvento(oEvento)
    
    def animaClick(self, boton=None):
        return self.ctx.oficial_animaClick(boton)
    
    def dameWidget(self, wN=None):
        return self.ctx.oficial_dameWidget(wN)
    
    def abreForm(self, oPaso=None):
        return self.ctx.oficial_abreForm(oPaso)
    
    def clickBoton(self, oPaso=None):
        return self.ctx.oficial_clickBoton(oPaso)
    
    def ponValorFLField(self, oPaso=None):
        return self.ctx.oficial_ponValorFLField(oPaso)
    
    def dameValor(self, valor=None):
        return self.ctx.oficial_dameValor(valor)
    
    def dameValorFLField(self, fN=None):
        return self.ctx.oficial_dameValorFLField(fN)
    
    def dameValorLabel(self, fN=None):
        return self.ctx.oficial_dameValorLabel(fN)
    
    def aceptaForm(self, oPaso=None):
        return self.ctx.oficial_aceptaForm(oPaso)
    
    def insertaRegistro(self, oPaso=None):
        return self.ctx.oficial_insertaRegistro(oPaso)
    
    def editaRegistro(self, oPaso=None):
        return self.ctx.oficial_editaRegistro(oPaso)
    
    def borraRegistro(self, oPaso=None):
        return self.ctx.oficial_borraRegistro(oPaso)
    
    def cierraForm(self, oPaso=None):
        return self.ctx.oficial_cierraForm(oPaso)
    
    def seleccionaReg(self, oPaso=None):
        return self.ctx.oficial_seleccionaReg(oPaso)
    
    def guardaValorCursor(self, oPaso=None):
        return self.ctx.oficial_guardaValorCursor(oPaso)
    
    def abrePestana(self, oPaso=None):
        return self.ctx.oficial_abrePestana(oPaso)
    
    def comprueba(self, oPaso=None):
        return self.ctx.oficial_comprueba(oPaso)
    
    def guardaValorSQL(self, oPaso=None):
        return self.ctx.oficial_guardaValorSQL(oPaso)
    
    def anadeFormPila(self, nombreF=None):
        return self.ctx.oficial_anadeFormPila(nombreF)
    
    def ponFormActual(self):
        return self.ctx.oficial_ponFormActual()
    
    def nombreFormActual(self):
        return self.ctx.oficial_nombreFormActual()
    
    def quitaFormPila(self):
        return self.ctx.oficial_quitaFormPila()
    
    def ponValores(self, cadena=None):
        return self.ctx.oficial_ponValores(cadena)
    
    def dameValorMemo(self, nombreVar=None):
        return self.ctx.oficial_dameValorMemo(nombreVar)
    
    def inicioBucle(self, oPaso=None):
        return self.ctx.oficial_inicioBucle(oPaso)
    
    def finBucle(self, oPaso=None):
        return self.ctx.oficial_finBucle(oPaso)
    

#/** @class_declaration head */
class head(oficial):
    def __init__(self, context=None):
        super(head, self).__init__(context)
    

#/** @class_declaration ifaceCtx */
class ifaceCtx(head):
    def __init__(self, context=None):
        super(ifaceCtx, self).__init__(context)
    

#/** @class_declaration FormInternalObj */
class FormInternalObj(FormDBWidget):
    
    #/** @class_definition FormInternalObj */
    def _class_init(self):
        self.iface = ifaceCtx(self)
    
    #/** @class_definition interna */
    def interna_init(self):
        return 
        debug(u"testing va")
        _i = self.iface
        _i.openDF(u"facturascli")
    
    #/** @class_definition oficial */
    def oficial_recibeEvento(self, tipo=None, emisor=None):
        _i = self.iface
        ignorado = False
        debug(ustr( u"Recibido evento " , tipo , u" desde " , emisor , u" " , _i.testing ))
        debug(_i.oEventoEsperado)
        if not _i.testing:
            debug(u"No testing")
            return True
        _i.log(sys.translate(u"Recibido evento %s desde %s") % (str(tipo), str(emisor)), u"evento")
        if tipo == u"formReady":
            debug(u"anadeFormPila")
            _i.anadeFormPila(emisor)
        elif tipo == u"formClosed":
            if _i.aPilaForms:
                debug(u"quitaFormPila")
                _i.quitaFormPila()
            else:
                ignorado = True
        elif _i.oEventoEsperado:
            debug(u"Evento esperado")
            if _i.oEventoEsperado[u"tipo"] != tipo or _i.oEventoEsperado[u"emisor"] != emisor:
                ignorado = True
                _i.log(sys.translate(u"Ignorado. Esperando evento %s desde %s") % (str(_i.oEventoEsperado[u"tipo"]), str(_i.oEventoEsperado[u"emisor"])), u"comentario")
            else:
                _i.oEventoEsperado = None
            
        
        else:
            debug(u"Sin evento esperado")
        
        if not ignorado:
            _i.oEventoEsperado = None #Aulla
            _i.ejecutaPaso()
    
    def oficial_anadeFormPila(self, nombreF=None):
        _i = self.iface
        if nombreF not in _i.aPilaForms:
            _i.aPilaForms.append(nombreF)
            _i.ponFormActual()
    
    def oficial_quitaFormPila(self):
        _i = self.iface
        if _i.aPilaForms:
            _i.aPilaForms.pop()
            _i.ponFormActual()
    
    def oficial_ponFormActual(self):
        _i = self.iface
        fN = _i.nombreFormActual()
        if fN:
            if sys.interactiveGUI() == u"Pineboo":
                #debug(ustr( u"10 primeras " , parseString(fN)[0:10] ))
                #debug(ustr( u"Si las quito " , parseString(fN)[(len(parseString(fN)) - (len(fN) - 10)):] ))
                if parseString(fN)[0:10] == u"formRecord":
                    accion = parseString(fN)[(len(parseString(fN)) - (len(fN) - 10)):]
                    _i.formActual = pineboolib.project.actions[accion].formrecord_widget.script.form
                else:
                    if parseString(fN)[0:4] == u"form":
                        accion = parseString(fN)[(len(parseString(fN)) - (len(fN) - 4)):]
                        #debug(ustr( u"accion = " , accion ))
                        _i.formActual = pineboolib.project.actions[accion].mainform_widget.script.form
                
            
            else:
                _i.formActual = eval(fN)
            
            _i.log(ustr( u"Form actual es " , fN ), u"form")
        
        else:
            _i.log(u"No hay form actual.", u"form")
            _i.formActual = False
        
        return True
    
    def oficial_nombreFormActual(self):
        _i = self.iface
        fN = False
        totalForms = len(_i.aPilaForms)
        if totalForms > 0:
            fN = _i.aPilaForms[totalForms - 1]
        return fN
    
    def oficial_lanzaTest(self, fN=None):
        _i = self.iface
        _i.log = formtt_test.iface.log
        if _i.oMemoria:
            del _i.oMemoria
            pass
        _i.oMemoria = { }
        if _i.oBucle:
            del _i.oBucle
            pass
        _i.oBucle = { }
        _i.oEventoEsperado = False
        if _i.aPilaForms:
            del _i.aPilaForms
            pass
        _i.aPilaForms = []
        if _i.aPasos:
            del _i.aPasos
            pass
        sPasos = File.read(fN)
        debug(sPasos)
        _i.aPasos = eval(sPasos)
        _i.testing = True
        _i.log(u"Lanza test", u"OK")
        _i.iPaso = 0
        _i.ejecutaPaso()
    
    def oficial_finTest(self, tipo=None):
        _i = self.iface
        _i.log(u"Fin test", tipo)
        _i.testing = False
    
    def oficial_esperarEvento(self, oPaso=None):
        _i = self.iface
        oEvento = False
        if u"esperarEvento" in oPaso:
            oEvento = oPaso[u"esperarEvento"]
        if _i.oEventoEsperado:
            del _i.oEventoEsperado
            _i.oEventoEsperado = False
        if oEvento:
            _i.oEventoEsperado = { }
            _i.oEventoEsperado[u"tipo"] = oEvento[u"tipo"]
            _i.oEventoEsperado[u"emisor"] = oEvento[u"emisor"]
        return True
    
    def oficial_ejecutaPaso(self):
        _i = self.iface
        debug(u"oficial_ejecutaPaso 1")
        if _i.oEventoEsperado:
            return 
        debug(u"oficial_ejecutaPaso 2")
        if _i.iPaso >= len(_i.aPasos):
            _i.finTest(u"OK")
            return 
        debug(u"oficial_ejecutaPaso 3")
        oPaso = _i.aPasos[_i.iPaso]
        tipo = oPaso[u"tipo"]
        _i.log(ustr( u"Paso " , _i.iPaso , u" tipo " , tipo ))
        if not _i.esperarEvento(oPaso):
            _i.finTest()
            return 
        if _i.fPaso:
            del _i.fPaso
            pass
        if sys.interactiveGUI() == u"Pineboo":
            _i.fPaso = getattr(fltesttest.iface, tipo)
        else:
            _i.fPaso = Function(u"oPaso", ustr( u"return fltesttest.iface." , tipo , u"(oPaso)" ))
        
        _i.iPaso += 1
        try:
            _i.fPaso(oPaso)
        except Exception as e:
            e = traceback.format_exc()
            debug(ustr( u"Error en paso: " , e ))
        
    
    def oficial_dameValor(self, valor=None):
        _i = self.iface
        valorRet = False
        if parseString(valor)[0:1] == u"$":
            vM = valor[(len(valor) - (len(valor) - 1)):]
            if vM in _i.oMemoria:
                valorRet = _i.oMemoria[vM]
        else:
            valorRet = valor
        
        return valorRet
    
    def oficial_abreForm(self, oPaso=None):
        _i = self.iface
        accion = oPaso[u"accion"]
        _i.log(sys.translate(u"Paso %s. Abre formulario maestro de %s") % (str(_i.iPaso), str(accion)))
        oPaso[u"esperarEvento"] = { u"tipo" : ( u"formReady" ) , u"emisor" : ( ustr( u"form" , accion ) ) , }
        _i.esperarEvento(oPaso)
        if sys.interactiveGUI() == u"Pineboo":
            aqApp.mainWidget().triggerAction("%s:%s:%s" % ("triggered()","openDefaultForm()",accion))
        else:
            sys.openMasterForm(accion)
        
        return True
        """
        list = AQObjectQueryList(0, u"QMainWindow", u"container", True, True)
        container = list.current()
        if container != None:
            aG = container.child(u"abanqActionGroup")
            recursiva = ( False if aG else True )
            aG = ( aG if aG else container )
            ac = aG.child(accion)
            debug(u"Llamada a omf")
            sys.openMasterForm(ac.name, ac.iconSet().pixmap())
            debug(u"Fin llamada a omf")
        
        return True
        """
    def oficial_seleccionaReg(self, oPaso=None):
        _i = self.iface
        campo = oPaso[u"campo"]
        valor = _i.dameValor(oPaso[u"valor"])
        _i.log(sys.translate(u"Paso %s. Selecciona fila donde %s = %s") % (str(_i.iPaso), str(campo), str(valor)))
        t = _i.dameWidget(u"tableDBRecords")
        if not t:
            _i.finTest(oPaso)
            return False
        t.refresh()
        c = t.cursor()
        pos = c.atFromBinarySearch(campo, valor)
        t.setCurrentRow(pos)
        _i.ejecutaPaso()
    
    def oficial_cierraForm(self, oPaso=None):
        _i = self.iface
        _i.log(sys.translate(u"Paso %s. Cancela formulario") % (str(_i.iPaso)))
        if not _i.oEventoEsperado:
            fN = _i.nombreFormActual()
            _i.oEventoEsperado = { u"tipo" : ( u"formClosed" ) , u"emisor" : ( fN ) , }
        _i.animaClick(u"pushButtonCancel")
    
    def oficial_aceptaForm(self, oPaso=None):
        _i = self.iface
        _i.log(sys.translate(u"Paso %s. Acepta formulario") % (str(_i.iPaso)))
        if not _i.oEventoEsperado:
            fN = _i.nombreFormActual()
            _i.oEventoEsperado = { u"tipo" : ( u"formClosed" ) , u"emisor" : ( fN ) , }
        _i.animaClick(u"pushButtonAccept")
    
    def oficial_insertaRegistro(self, oPaso=None):
        _i = self.iface
        _i.log(sys.translate(u"Paso %s. Inserta registro") % (str(_i.iPaso)))
        tN = None
        if u"fltabledb" in oPaso:
            tN = oPaso[u"fltabledb"]
        else:
            tN = u"tableDBRecords"
        
        t = _i.dameWidget(tN)
        if not t:
            _i.log(sys.translate(u"No encuentra tabla %s") % (str(tN)), u"ERROR")
            _i.finTest()
            return False

        t.insertRecord()
    
    def oficial_editaRegistro(self, oPaso=None):
        _i = self.iface
        _i.log(sys.translate(u"Paso %s. Edita registro") % (str(_i.iPaso)))
        tN = None
        if u"fltabledb" in oPaso:
            tN = oPaso[u"fltabledb"]
        else:
            tN = u"tableDBRecords"
        
        t = _i.dameWidget(tN)
        if not t:
            _i.log(sys.translate(u"No encuentra tabla %s") % (str(tN)), u"ERROR")
            _i.finTest()
            return False

        t.editRecord()
    
    def oficial_borraRegistro(self, oPaso=None):
        _i = self.iface
        _i.log(sys.translate(u"Paso %s. Borra registro") % (str(_i.iPaso)))
        tN = None
        if u"fltabledb" in oPaso:
            tN = oPaso[u"fltabledb"]
        else:
            tN = u"tableDBRecords"
        
        t = _i.dameWidget(tN)
        if not t:
            _i.log(sys.translate(u"No encuentra tabla %s") % (str(tN)), u"ERROR")
            _i.finTest()
            return False

        t.deleteRecord()
    
    def oficial_clickBoton(self, oPaso=None):
        _i = self.iface
        boton = oPaso[u"boton"]
        _i.log(sys.translate(u"Paso %s. Pulsa botÃ³n %s") % (str(_i.iPaso), str(boton)))
        _i.animaClick(boton)
    
    def oficial_animaClick(self, boton=None):
        _i = self.iface
        b = _i.dameWidget(boton)
        if not b:
            return False
        b.animateClick()
    
    def oficial_dameWidget(self, wN=None):
        _i = self.iface
        if not _i.formActual:
            return False
        w = _i.formActual.child(wN)
        if not w:
            _i.log(ustr( u"dameWidget: No existe el control " , wN ), u"error")
            return False
        return w
    
    def oficial_ponValorFLField(self, oPaso=None):
        _i = self.iface
        fN = oPaso[u"FLField"]
        valor = oPaso[u"valor"]
        _i.log(sys.translate(u"Paso %s. Pon valor %s en FLField %s") % (str(_i.iPaso), str(valor), str(fN)))
        f = _i.dameWidget(fN)
        if not f:
            _i.finTest(oPaso)
            return False
        debug(u"setValue")
        f.setValue(valor)
        debug(u"setValueFin")
        _i.ejecutaPaso()
    
    def oficial_dameValorFLField(self, fN=None):
        _i = self.iface
        f = _i.dameWidget(fN)
        if not f:
            return False
        return f.value()
    
    def oficial_dameValorLabel(self, fN=None):
        _i = self.iface
        f = _i.dameWidget(fN)
        if not f:
            return False
        return f.text
    
    def oficial_guardaValorCursor(self, oPaso=None):
        _i = self.iface
        variable = oPaso[u"var"]
        campo = oPaso[u"campo"]
        _i.log(sys.translate(u"Paso %s. Guarda valor de cursor %s en %s") % (str(_i.iPaso), str(campo), str(variable)))
        if not _i.formActual:
            _i.finTest(oPaso)
            return False
        cursor = _i.formActual.cursor()
        if not cursor:
            _i.finTest(oPaso)
            return False
        _i.log(sys.translate(u"Guardando en memoria %s = %s") % (str(variable), str(cursor.valueBuffer(campo))), u"comentario")
        _i.oMemoria[variable] = cursor.valueBuffer(campo)
        _i.ejecutaPaso()
    
    def oficial_abrePestana(self, oPaso=None):
        _i = self.iface
        wN = oPaso[u"fltabwidget"]
        pestana = oPaso[u"pestana"]
        _i.log(sys.translate(u"Paso %s. Abre pestaÃ±a %s de %s") % (str(_i.iPaso), str(pestana), str(wN)))
        tW = _i.dameWidget(wN)
        if not tW:
            _i.finTest(oPaso)
            return False
        tW.showPage(pestana)
        _i.ejecutaPaso()
    
    def oficial_guardaValorSQL(self, oPaso=None):
        _i = self.iface
        select = oPaso[u"select"]
        from_ = oPaso[u"from"]
        where = oPaso[u"where"]
        varP = oPaso[u"var"]
        _i.log(sys.translate(u"Paso %s. Guarda valor SQL en %s") % (str(_i.iPaso), str(varP)))
        rCampo = RegExp(u"/@[_A-Za-z][_A-Za-z0-9]*/g")
        rCampo.search(where)
        i = 0
        rVariable = None
        variable = None
        valorMemo = None
        debug(ustr( u"Buscando en " , where ))
        while rCampo.cap(i):
            debug(ustr( u"Encontrado " , rCampo.cap(i) ))
            rVariable = RegExp(rCampo.cap(i))
            rVariable.global_ = True
            variable = parseString(rCampo.cap(i))[(len(parseString(rCampo.cap(i))) - (len(rCampo.cap(i)) - 1)):]
            debug(ustr( u"variable " , variable ))
            if variable in _i.oMemoria:
                if sys.interactiveGUI() == u"Pineboo":
                    where = parseString(where).replace(rCampo.cap(i), _i.oMemoria[variable])
                else:
                    where = parseString(where).replace(rVariable, _i.oMemoria[variable])
                
                debug(ustr( u"where " , where ))
            
            else:
                _i.log(sys.translate(u"No se encontrÃ³ el valor de la variable %s") % (str(variable)), u"error")
                _i.finTest()
                return False
            
            i += 1
        
        q = FLSqlQuery()
        q.setSelect(select)
        q.setFrom(from_)
        q.setWhere(where)
        _i.log(ustr( u"Lanzando " , q.sql() ), u"comentario")
        if not q.exec_():
            debug(u"!exec")
            _i.finTest()
            return False
        if not q.first():
            debug(u"!first")
            _i.finTest()
            return False
        _i.log(ustr( u"Guardando valor " , q.value(0) , u" en " , varP ), u"comentario")
        _i.oMemoria[varP] = q.value(0)
        _i.ejecutaPaso()
    
    def oficial_ponValores(self, s=None):
        _i = self.iface
        cadena = parseString(s)
        rCampo = RegExp(u"/@[_A-Za-z][_A-Za-z0-9]*/g")
        rCampo.search(cadena)
        i = 0
        rVariable = None
        variable = None
        debug(ustr( u"Buscando en " , cadena ))
        while rCampo.cap(i):
            debug(ustr( u"Encontrado " , rCampo.cap(i) ))
            rVariable = RegExp(rCampo.cap(i))
            rVariable.global_ = True
            variable = parseString(rCampo.cap(i))[(len(parseString(rCampo.cap(i))) - (len(rCampo.cap(i)) - 1)):]
            debug(ustr( u"variable " , variable ))
            valor = _i.dameValorMemo(variable)
            if valor != None:
                if sys.interactiveGUI() == u"Pineboo":
                    cadena = parseString(cadena).replace(rCampo.cap(i), parseString(valor))
                else:
                    cadena = parseString(cadena).replace(rVariable, valor)
                
                debug(ustr( u"cadena " , cadena ))
            
            else:
                _i.log(sys.translate(u"No se encontrÃ³ el valor de la variable %s") % (str(variable)), u"error")
                _i.finTest()
                return False
            
            i += 1
        
        return cadena
    
    def oficial_dameValorMemo(self, nombreVar=None):
        _i = self.iface
        if not ( nombreVar in _i.oMemoria ):
            return None
        return _i.oMemoria[nombreVar]
    
    def oficial_comprueba(self, oPaso=None):
        _i = self.iface
        vReal = None
        vTest = None
        varR = None
        vTest = _i.ponValores(oPaso[u"valor"])
        if oPaso[u"tipoassert"] == u"FLField":
            varR = oPaso[u"FLField"]
            vReal = _i.dameValorFLField(oPaso[u"FLField"])
        else:
            if oPaso[u"tipoassert"] == u"label":
                vReal = _i.dameValorLabel(oPaso[u"label"])
                varR = oPaso[u"label"]
            else:
                if oPaso[u"tipoassert"] == u"memo":
                    varR = ustr( u"@" , oPaso[u"memo"] )
                    vReal = _i.dameValorMemo(oPaso[u"memo"])
            
        
        _i.log(sys.translate(u"Paso %s. Comprueba %s = %s") % (str(_i.iPaso), str(varR), str(vTest)))
        if isNaN(vReal):
            vReal = parseString(vReal)
        else:
            vReal = parseFloat(vReal)
        
        if isNaN(vTest):
            vTest = parseString(vTest)
        else:
            vTest = parseFloat(vTest)
        
        debug(ustr( u"vReal = '" , vReal , u"', vTest = '" , vTest , u"'" ))
        if vReal == vTest:
            _i.log(u"Assert %s = %s comprobado" % (str(vReal), str(vTest)), u"OK")
            _i.ejecutaPaso()
        else:
            _i.log(u"Assert %s = %s falló" % (str(vReal), str(vTest)), u"error")
            _i.finTest()
        
    
    def oficial_inicioBucle(self, oPaso=None):
        _i = self.iface
        nombre = oPaso[u"nombre"]
        max = parseFloat(oPaso[u"max"])
        _i.oBucle[nombre] = { u"max" : ( max ) , u"vez" : ( 0 ) , u"indice" : ( _i.iPaso ) , }
        _i.ejecutaPaso()
    
    def oficial_finBucle(self, oPaso=None):
        _i = self.iface
        nombre = oPaso[u"nombre"]
        if not ( nombre in _i.oBucle ):
            _i.log(sys.translate(u"No se encontró el valor de la variable %s") % (str(variable)), u"error")
            _i.finTest()
        _i.oBucle[nombre][u"vez"] += 1
        if _i.oBucle[nombre][u"vez"] < _i.oBucle[nombre][u"max"]:
            _i.iPaso = _i.oBucle[nombre][u"indice"]
        _i.ejecutaPaso()
    


form = None

