#fonction d'interpolation permettant de passer de la sensibilité en dBm au débit binaire

def interpolation (sensibility):
    #-93 dBm == 6 Mb/s
    #-73 dBm == 54 Mb/s
    #y = 6 + 2.4(x + 93)
    
    return 6 + 2.4(sensibility + 93)