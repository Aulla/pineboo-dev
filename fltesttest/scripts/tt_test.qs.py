# -*- coding: utf-8 -*-
from pineboolib.qsa import *

#/** @file */

#/** @class_declaration interna */
class interna(object):
    ctx = Object()
    def __init__(self, context=None):
        self.ctx = context
    
    def init(self):
        return self.ctx.interna_init()
    

#/** @class_declaration oficial */
class oficial(interna):
    def __init__(self, context=None):
        super(oficial, self).__init__(context)
    
    def tbnFichero_clicked(self):
        return self.ctx.oficial_tbnFichero_clicked()
    
    def tbnLanzar_clicked(self):
        return self.ctx.oficial_tbnLanzar_clicked()
    
    def log(self, msg=None, tipo=None):
        return self.ctx.oficial_log(msg, tipo)
    

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
        _i = self.iface
        connect(self.child(u"tbnFichero"), u"clicked()", _i, u"tbnFichero_clicked")
        connect(self.child(u"tbnLanzar"), u"clicked()", _i, u"tbnLanzar_clicked")
        ultimoTest = AQUtil.readSettingEntry(u"scripts/fltesttest/ultimoTest")
        if ultimoTest:
            self.child(u"ledRutaFichero").text = ultimoTest
    
    #/** @class_definition oficial */
    def oficial_tbnFichero_clicked(self):
        _i = self.iface
        fN = FileDialog.getOpenFileName(u"*.test")
        if not fN:
            return 
        debug(ustr( u"fN " , fN ))
        AQUtil.writeSettingEntry(u"scripts/fltesttest/ultimoTest", fN)
        self.child(u"ledRutaFichero").text = fN
    
    def oficial_tbnLanzar_clicked(self):
        fN = self.child(u"ledRutaFichero").text
        if not fN:
            return 
        self.child(u"log").text = u""
        fltesttest.iface.lanzaTest(fN)
    
    def oficial_log(self, msg=None, tipo=None):
        _i = self.iface
        d = Date()
        texto = ustr( parseString(d) , u": " , msg )
        debug(ustr( u"Test log = " , texto ))
        if tipo == u"error":
            texto = ustr( u"<font color=#990000>" , texto , u"</font>" )
        else:
            if tipo == u"OK":
                texto = ustr( u"<font color=#009900>" , texto , u"</font>" )
            else:
                if tipo == u"form":
                    texto = ustr( u"<font color=#000099>" , texto , u"</font>" )
                else:
                    if tipo == u"evento":
                        texto = ustr( u"<font color=#EE82EE>" , texto , u"</font>" )
                    else:
                        if tipo == u"comentario":
                            texto = ustr( u"<font color=#CCCCCC>" , texto , u"</font>" )
                    
                
            
        
        self.child(u"log").append(texto)
    


form = None
