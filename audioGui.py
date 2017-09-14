#!/usr/bin/python
# -*- encoding: utf-8 -*-

import pygtk
import gtk
from audiorecorder import *


class MenuExample(object):

    def __init__(self):

        #neues Objekt
        self.record = Record(None, None, "fdp", None)
        
        #Fenster anlegen
        window = gtk.Window()
        window.connect("destroy", self.destroy)
        window.set_title("Audiorecorder")
        #self.window.set_default_size(400, 300)
        window.set_position(gtk.WIN_POS_CENTER_ALWAYS)

#############################################
#MenuBar
        # erzeuge Menubar mit Top-items
        menuBar = gtk.MenuBar()
        fileI = gtk.MenuItem('File')
        aboutI = gtk.MenuItem('About')

        # FileMenu bauen
        fileMenu = gtk.Menu()
        fileI.set_submenu(fileMenu)

        # Quit
        acc = gtk.AccelGroup()
        window.add_accel_group(acc)

        quitImg = gtk.ImageMenuItem(gtk.STOCK_QUIT, acc)
        key, modifier = gtk.accelerator_parse('Q')
        quitImg.add_accelerator("activate", acc, key, modifier,
                                gtk.ACCEL_VISIBLE)
        # Exit-Funktion
        quitImg.connect('activate', lambda x: gtk.main_quit())
        fileMenu.append(quitImg)

        #About
        aboutI.connect('activate', self.showAbout)

        # hänge es an die Menubar und packe alles in eine vBox
        menuBar.append(fileI)
        menuBar.append(aboutI)
        box = gtk.VBox(False, 0)
        box.pack_start(menuBar, False, False, 0)
        window.add(box)

#End MenuBar
############################################################
# Window/Box

        boxMain = gtk.HBox(True, 5)

# Left ######

        frameRecord = gtk.Frame('Record')
        frameRecord.set_border_width(0)

        boxL = gtk.VBox(False, 5)
        boxL.set_border_width(5)

        box1 = gtk.VBox(True, 5)

        box11 = gtk.HBox()
        labelURL = gtk.Label("URL: ")
        link = gtk.Entry()

        link.connect('changed', self.linkEingabe)
        box11.pack_start(labelURL, False, False, 0)
        box11.pack_end(link, True, True, 0)

        box12 = gtk.HBox()
        labelLength = gtk.Label("Duration: ")
        length = gtk.Entry()
        length.connect('changed', self.lengthEingabe)
        box12.pack_start(labelLength, False, False, 0)
        box12.pack_end(length, True, True, 0) 

        box13 = gtk.HBox()
        labelFName = gtk.Label("Filename: ")
        fname = gtk.Entry()
        fname.connect('changed', self.fnameEingabe)
        box13.pack_start(labelFName, False, False, 0)
        box13.pack_end(fname, True, True, 0)

        box14 = gtk.HBox()
        labelBitrate = gtk.Label("Bitrate: ")
        bitrate = gtk.Entry()
        bitrate.connect('changed', self.bitrateEingabe)
        box14.pack_start(labelBitrate, False, False, 0)
        box14.pack_end(bitrate, True, True, 0)       

        box1.pack_start(box11, False, False, 0)
        box1.pack_start(box12, False, False, 0)
        box1.pack_start(box13, False, False, 0)
        box1.pack_start(box14, False, False, 0)

        boxL.pack_start(box1, False, False, 5)              

        box2 = gtk.HBox(False, 5)

        buttonRec = gtk.Button('Record')
        buttonRec.connect('clicked', self.newRecord)

        buttonAddDB = gtk.Button('Add to Database')
        buttonAddDB.connect('clicked', self.newEntryDB)

        box2.pack_start(buttonRec)
        box2.pack_start(buttonAddDB)

        boxL.pack_start(box2, False, False, 5)

        frameRecord.add(boxL)

        boxMain.pack_start(frameRecord, False, False, 10)

# right ########

        frameData = gtk.Frame('Data')
        frameData.set_border_width(0)

        boxR = gtk.VBox(False, 5)
        boxR.set_border_width(5)

        showData = gtk.Notebook()

        labelDB = gtk.Label('Database')

        scrollTable = gtk.ScrolledWindow()
        scrollTable.set_shadow_type(gtk.SHADOW_OUT)
        scrollTable.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)

        self.storeDB = gtk.ListStore(str, str, int, str)

        self.fillStore()
        pageDB = gtk.TreeView(model=self.storeDB)

        colNames = ('Name', 'URL', 'Bitrate', 'Format')
        for i in range(4):
            renTex = gtk.CellRendererText()
            colDB = gtk.TreeViewColumn(colNames[i], renTex, text=i)
            colDB.set_max_width(100)
            pageDB.append_column(colDB)

        scrollTable.add(pageDB)
        showData.append_page(scrollTable, labelDB)

        labelRec = gtk.Label('Record')

        scrollTable2 = gtk.ScrolledWindow()
        scrollTable2.set_shadow_type(gtk.SHADOW_OUT)
        scrollTable2.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)

        self.storeRec = gtk.ListStore(str)
        
        self.fillRec()
        pageRec = gtk.TreeView(model=self.storeRec)

        colNames2 = ('File')
        for i in range(1):
            rentexRec = gtk.CellRendererText()
            colRec = gtk.TreeViewColumn(colNames2, rentexRec, text=i)
            colRec.set_max_width(100)
            pageRec.append_column(colRec)

        scrollTable2.add(pageRec)
        showData.append_page(scrollTable2, labelRec)

        boxR.pack_start(showData, False, False, 5)

        frameData.add(boxR)

        boxMain.pack_start(frameData, False, False, 10)

        box.pack_start(boxMain, False, False, 5)

############################################################
#End GUI

        window.show_all()

############################################################
#Window Functions

    def destroy(self, widget):
        gtk.main_quit()

############################################################
#MenuBar Functions

    def showAbout(self, widget):
        ad = gtk.AboutDialog()
        ad.set_authors(('KatHa Kana', 'Dev'))
        ad.set_website('http usw nomnomnom')
        ad.set_copyright('(C) 2013')
        ad.set_version('0.1')
        ad.set_program_name('Audiorecorder')
        ad.run()
        ad.destroy()

##############################################################
# Window/Box Functions

    def linkEingabe(self, widget):
        self.record.setLink(widget.get_text())

    def lengthEingabe(self, widget):
        try:
            self.record.setLength(int(widget.get_text()))
        except:
            pass

    def fnameEingabe(self, widget):
        self.record.setFilename(widget.get_text())

    def bitrateEingabe(self, widget):
        try:
            self.record.setBitrate(int(widget.get_text()))
        except:
            pass

    def newRecord(self, widget):
        if self.record.link != None and self.record.length != None and self.record.bitrate != None:
            self.record.recordStream()
        else:
            self.popUp()

    def popUp(self): 
        label = gtk.Label("Please fill out the blank boxes")
        dialog = gtk.Dialog("Error Message", None,
                   gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                   (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        dialog.vbox.pack_start(label)
        label.show()
        response = dialog.run()
        dialog.destroy()
        #gtk.modal freezes the main window

    def fillStore(self):
        dataInStore = self.record.useDB()

        if dataInStore is not None:
            self.storeDB.clear()
            for row in dataInStore:
                self.storeDB.append(row)

        return self.storeDB

    def fillRec(self):
        dataInStore = self.record.showRecords()

        if dataInStore is not None:
            self.storeRec.clear()
            for rec in dataInStore:
                self.storeRec.append([rec])

        return self.storeRec

    def newEntryDB(self, widget):
        if self.record.link != None and self.record.filename != None and self.record.bitrate != None:
            self.record.entryDB()
        else:
            self.popUp()
        

if __name__ == '__main__':
    menuExample = MenuExample()
    gtk.main()

    