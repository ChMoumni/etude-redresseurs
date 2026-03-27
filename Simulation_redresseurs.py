import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------- Section 1 --------------------------------------------------

""" Fonction qui génère le signal sinusoïdal d'entrée que l'on veut filtrer """
def entree(t, f=50, Eo=230): 
    U = Eo*np.sqrt(2)*np.cos(2*(np.pi)*f*t)
    return U

""" Fonction diode idéale """
def diode_ideale(U):
    Us = np.where(U > 0, U, 0)
    return Us

""" Fonction pont de Graetz idéal """
def graetz_ideale(U):
    return np.abs(U)

""" Fonction calculant la valeur moyenne et efficace de la tension """
def valeur_moy_eff(U):
    U_moy = np.mean(U)
    U_eff = np.sqrt(np.mean(U**2))
    return U_moy, U_eff

""" Fonction filtre moyenneur """
def filtre(U):
    U_filtre = np.zeros_like(U)
    for i in range(len(U)):
        U_filtre[i] = np.mean(U)
    return U_filtre

""" Fonction qui effectue l'analyse spectrale """
def spectre_frequentiel(t, U_dt, fe=10000):
    n = len(t)  # longueur du signal 
    d = 1/fe    # période d'échantillonnage
    U_df = np.fft.rfft(U_dt)  # signal dans le domaine fréquentiel
    freq = np.fft.rfftfreq(n, d)
    ampl = abs(U_df)
    return freq, ampl

#-------------------------------------------- Section 2 --------------------------------------------------

""" Fonction redresseur mono-alternance"""
def Redresseur_mono_alternance(t, f, Uo):
    # signal d'entrée
    Ue = entree(t, f, Uo)
    # valeur moyenne et efficace du signal d'entrée
    Ue_moy, Ue_eff = valeur_moy_eff(Ue)

    # signal de sortie, après la diode
    Us = diode_ideale(Ue)
    # valeur moyenne et efficace du signal de sortie
    Us_moy, Us_eff = valeur_moy_eff(Us)

    return Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff

""" Fonction redresseur double-alternance """
def Redresseur_double_alternance(t, f, Uo):
    # signal d'entrée
    Ue = entree(t, f, Uo)
    # valeur moyenne et efficace du signal d'entrée
    Ue_moy, Ue_eff = valeur_moy_eff(Ue)

    # signal de sortie, après le pont de Graetz
    Us = graetz_ideale(Ue)
    # valeur moyenne et efficace du signal de sortie
    Us_moy, Us_eff = valeur_moy_eff(Us)

    return Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff

""" Fonction pont de Graetz avec filtrage capacitif"""
def Redresseur_double_alternance_filtrage(t, f, Uo):
    # signal d'entrée
    Ue = entree(t, f, Uo)
    # valeur moyenne et efficace du signal d'entrée
    Ue_moy, Ue_eff = valeur_moy_eff(Ue)

    # signal de sortie, après le pont de Graetz
    Ug = graetz_ideale(Ue)
    # valeur moyenne et efficace du signal de sortie, après le pont de Graetz
    Ug_moy, Ug_eff = valeur_moy_eff(Ug)

    # signal de sortie, après le filtre RC
    Us = filtre(Ug)
    # valeur moyenne
    Us_moy, Us_eff = valeur_moy_eff(Us)

    return Ue, Ue_moy, Ue_eff, Ug, Ug_moy, Ug_eff, Us, Us_moy, Us_eff

#-------------------------------------------- Section 3 --------------------------------------------------

""" Fonction qui trace les signaux ainsi que leurs spectres (Redresseur double-alternance et mono-alternance) """
def tracer_signaux_et_leurs_spectres(t, Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff, fe=10000):
    plt.figure(figsize=(16,8))

    # courbe du signal d'entrée
    plt.subplot(2,2,1)
    plt.plot(t, Ue, label="Signal d'entrée (Ue)", color="b")
    # petit encadré affichant les valeurs moyenne et efficace du signal
    text_Ue = f"Ue_moy = {round(Ue_moy,2)} V \nUe_eff = {round(Ue_eff,2)} V"
    plt.annotate(text_Ue, xy=(0.05,0.05), xycoords="axes fraction", fontsize=10, bbox={"boxstyle":"round", "facecolor":"blue", "alpha":0.2})

    plt.title("Signal d'entrée")
    plt.xlabel("Temps (s)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.grid(True)

    # spectre de fréquence du signal d'entrée
    freq_Ue, ampl_Ue = spectre_frequentiel(t, Ue, fe)
    plt.subplot(2,2,3)
    plt.plot(freq_Ue, 20*np.log10(ampl_Ue), color="b")
    plt.title("Spectre de fréquence du signal d'entrée")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.xlim(0,1000)
    plt.grid(True)

    #------------------------------------------------------------------------------------------

    # courbe du signal de sortie
    plt.subplot(2,2,2)
    plt.plot(t, Us, label="Signal de sortie (Us)", color="r")
    # créer une symétrie autour du 0 de l'axe des ordonnées pour le centrer et mieux comparer les courbes
    plt.ylim(-350, 350)
    # petit encadré affichant les valeurs moyenne et efficace du signal
    text_Us = f"Us_moy = {round(Us_moy,2)} V \nUs_eff = {round(Us_eff,2)} V"
    plt.annotate(text_Us, xy=(0.05,0.05), xycoords="axes fraction", fontsize=10, bbox={"boxstyle":"round", "facecolor":"red", "alpha":0.2})

    plt.title("Signal de sortie")
    plt.xlabel("Temps (s)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.grid(True)

    # spectre de fréquence du signal de sortie
    freq_Us, ampl_Us = spectre_frequentiel(t, Us, fe)
    plt.subplot(2,2,4)
    plt.plot(freq_Us, 20*np.log10(ampl_Us), color="r")
    plt.title("Spectre de fréquence du signal de sortie")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.xlim(0,1000)
    plt.grid(True)
    
    plt.tight_layout()

""" Fonction qui trace les signaux ainsi que leurs spectres (Redresseur double-alternance avec filtrage capacitif) """
def tracer_signaux_et_leurs_spectres_Redresseur_double_alternance_filtrage(t, Ue, Ue_moy, Ue_eff, Ug, Ug_moy, Ug_eff, Us, Us_moy, Us_eff, fe=10000):
    plt.figure(figsize=(16,8))

    # courbe du signal d'entrée
    plt.subplot(2,3,1)
    plt.plot(t, Ue, label="Signal d'entrée (Ue)", color="b")
    # petit encadré affichant les valeurs moyenne et efficace du signal
    text_Ue = f"Ue_moy = {round(Ue_moy,2)} V \nUe_eff = {round(Ue_eff,2)} V"
    plt.annotate(text_Ue, xy=(0.05,0.05), xycoords="axes fraction", fontsize=10, bbox={"boxstyle":"round", "facecolor":"blue", "alpha":0.2})

    plt.title("Signal d'entrée")
    plt.xlabel("Temps (s)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.grid(True)

    # spectre de fréquence du signal d'entrée
    freq_Ue, ampl_Ue = spectre_frequentiel(t, Ue, fe)
    plt.subplot(2,3,4) 
    plt.plot(freq_Ue, 20*np.log10(ampl_Ue), color="b")
    plt.title("Spectre de fréquence du signal d'entrée")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.xlim(0,1000)
    plt.grid(True)

    #------------------------------------------------------------------------------------------

    # courbe du signal de sortie au pont de Graetz
    plt.subplot(2,3,2)
    plt.plot(t, Ug, label="Signal de sortie (Ug)", color="r")
    # créer une symétrie autour du 0 de l'axe des ordonnées pour le centrer et mieux comparer les courbes
    plt.ylim(-350, 350)
    # petit encadré affichant les valeurs moyenne et efficace du signal
    text_Ug = f"Ug_moy = {round(Ug_moy,2)} V \nUg_eff = {round(Ug_eff,2)} V"
    plt.annotate(text_Ug, xy=(0.05,0.05), xycoords="axes fraction", fontsize=10, bbox={"boxstyle":"round", "facecolor":"red", "alpha":0.2})

    plt.title("Signal de sortie au pont de Graetz")
    plt.xlabel("Temps (s)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.grid(True)

    # spectre de fréquence du signal de sortie au pont de Graetz
    freq_Ug, ampl_Ug = spectre_frequentiel(t, Ug, fe)
    plt.subplot(2,3,5)
    plt.plot(freq_Ug, 20*np.log10(ampl_Ug), color="r")
    plt.title("Spectre de fréquence du signal de sortie au pont de Graetz")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.xlim(0,1000)
    plt.grid(True)

    #------------------------------------------------------------------------------------------

    # courbe du signal de sortie (après le filtre)
    plt.subplot(2,3,3)
    plt.plot(t, Us, label="Signal de sortie (Us)", color="green")
    # créer une symétrie autour du 0 de l'axe des ordonnées pour le centrer et mieux comparer les courbes
    plt.ylim(-350, 350)
    # petit encadré affichant les valeurs moyenne et efficace du signal
    text_Us = f"Us_moy = {round(Us_moy,2)} V \nUs_eff = {round(Us_eff,2)} V"
    plt.annotate(text_Us, xy=(0.05,0.05), xycoords="axes fraction", fontsize=10, bbox={"boxstyle":"round", "facecolor":"green", "alpha":0.2})

    plt.title("Signal de sortie filtré")
    plt.xlabel("Temps (s)")
    plt.ylabel("Tension (V)")
    plt.legend()
    plt.grid(True)

    # spectre de fréquence du signal de sortie (après le filtre)
    freq_Us, ampl_Us = spectre_frequentiel(t, Us, fe)
    plt.subplot(2,3,6)
    plt.plot(freq_Us, 20*np.log10(ampl_Us), color="green")
    plt.title("Spectre de fréquence du signal de sortie filtré")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Amplitude (dB)")
    plt.xlim(0,1000)
    plt.grid(True)
    
    plt.tight_layout()

""" Fonction qui demande à l'utilisateur quelle redresseur il veut """
def menu():
    fe = 5000  # fréquence d'échantillonnage
    d = 3*(1/50)  # 3 périodes
    t = np.arange(0, d, 1/fe)

    choix = int(input("Faites votre choix : " 
                     "\n1 : Redresseur mono-alternance " 
                     "\n2 : Redresseur double-alternance " 
                     "\n3 : Redresseur double-alternance avec filtre " 
                     "\nChoix : "))

    if choix == 1:
        Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff = Redresseur_mono_alternance(t, 50, 230)
        tracer_signaux_et_leurs_spectres(t, Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff, fe)
        plt.savefig("Redresseur_mono_alternance.pdf")
        plt.show()

    elif choix == 2:
        Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff = Redresseur_double_alternance(t, 50, 230)
        tracer_signaux_et_leurs_spectres(t, Ue, Ue_moy, Ue_eff, Us, Us_moy, Us_eff, fe)
        plt.savefig("Pont_de_Graetz.pdf")
        plt.show()

    elif choix == 3:
        Ue, Ue_moy, Ue_eff, Ug, Ug_moy, Ug_eff, Us, Us_moy, Us_eff = Redresseur_double_alternance_filtrage(t, 50, 230)
        tracer_signaux_et_leurs_spectres_Redresseur_double_alternance_filtrage(t, Ue, Ue_moy, Ue_eff, Ug, Ug_moy, Ug_eff, Us, Us_moy, Us_eff, fe)
        plt.savefig("Pont_de_Graetz_filtre.pdf")
        plt.show()

menu()








