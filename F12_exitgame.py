def exit():
    #variabel untuk melakukan save atau tidak
    save = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ?')
    if save == 'Y' or save == 'y':
        return(True)   #return True berarti jalankan save
    elif save == 'N' or save == 'n':
        return(False)   #return false berarti jangan jalankan save