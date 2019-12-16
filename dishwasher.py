import numpy as np
import skfuzzy as fuzz
# Plot
import matplotlib.pylab as plt
# Plot the result in pretty 3D with alpha blending
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

# Input
x_bulasik_miktar = np.arange(0,101,1)
x_kirlilik_derece = np.arange(0,101,1)
x_bulasik_cins = np.arange(0,101,1)

# Output
yikama_zaman = np.arange(30,161,1)
deterjan_miktar = np.arange(0,101,1)
su_sicaklik = np.arange(35,71,1)
ust_pompa = np.arange(2100, 3501, 1)
alt_pompa = np.arange(2100, 3501, 1)

# Input MF
bulasik_miktar_az = fuzz.trimf(x_bulasik_miktar, [0,0,35])
bulasik_miktar_ort = fuzz.trimf(x_bulasik_miktar, [15,50,85])
bulasik_miktar_cok = fuzz.trimf(x_bulasik_miktar, [65,100,100])

kirlilik_derece_az = fuzz.trimf(x_kirlilik_derece, [0,0,35])
kirlilik_derece_ort = fuzz.trimf(x_kirlilik_derece, [15,50,85])
kirlilik_derece_cok = fuzz.trimf(x_kirlilik_derece, [65,100,100])

bulasik_cins_has = fuzz.trimf(x_bulasik_cins, [0,0,35])
bulasik_cins_kar = fuzz.trimf(x_bulasik_cins, [15,50,85])
bulasik_cins_guc = fuzz.trimf(x_bulasik_cins, [65,100,100])

# Output MF
# cok kısa, kısa, orta, uzun, cok uzun
yikama_zaman_ck = fuzz.trimf(yikama_zaman, [30,30,60])
yikama_zaman_k = fuzz.trimf(yikama_zaman, [40,65,90])
yikama_zaman_o = fuzz.trimf(yikama_zaman, [70,95,120])
yikama_zaman_u = fuzz.trimf(yikama_zaman, [100,125,150])
yikama_zaman_cu = fuzz.trimf(yikama_zaman, [130,160,160])
# çok az, az, normal, çok, çok fazla
deterjan_miktar_ca = fuzz.trimf(deterjan_miktar, [0,0,17.5])
deterjan_miktar_a = fuzz.trimf(deterjan_miktar, [7.5,25,42.5])
deterjan_miktar_n = fuzz.trimf(deterjan_miktar, [32.5,50,67.5])
deterjan_miktar_c = fuzz.trimf(deterjan_miktar, [57.5,75,92.5])
deterjan_miktar_cf = fuzz.trimf(deterjan_miktar, [82.5,100,100])
# düşük, normal, yüksek
su_sicaklik_dus = fuzz.trimf(su_sicaklik, [35,35,50])
su_sicaklik_nor = fuzz.trimf(su_sicaklik, [37.5,52,67.5])
su_sicaklik_yuk = fuzz.trimf(su_sicaklik, [55,71,71])
# çok düşük, düşük, orta, yüksek, çok yüksek
ust_pompa_cd = fuzz.trimf(ust_pompa, [2100, 2100, 2400])
ust_pompa_d = fuzz.trimf(ust_pompa, [2300, 2500, 2700])
ust_pompa_o = fuzz.trimf(ust_pompa, [2600, 2800, 3000])
ust_pompa_y = fuzz.trimf(ust_pompa, [2900, 3100, 3300])
ust_pompa_cy = fuzz.trimf(ust_pompa, [3200, 3500, 3500])
# çok düşük, düşük, orta, yüksek, çok yüksek
alt_pompa_cd = fuzz.trimf(alt_pompa, [2100, 2100, 2400])
alt_pompa_d = fuzz.trimf(alt_pompa, [2300, 2500, 2700])
alt_pompa_o = fuzz.trimf(alt_pompa, [2600, 2800, 3000])
alt_pompa_y = fuzz.trimf(alt_pompa, [2900, 3100, 3300])
alt_pompa_cy = fuzz.trimf(alt_pompa, [3200, 3500, 3500])


# *Kullanıcı Girişleri
input_miktar = 0
input_kirlilik = 0
input_cins = 0
# Sonuçlar (global olarak tanımlanmalı)
zaman_defuzz = zaman_activation = deterjan_defuzz = deterjan_activation = sicaklik_defuzz = sicaklik_activation = alt_pompa_defuzz = alt_pompa_activation = ust_pompa_defuzz = ust_pompa_activation = 0
zaman_aggregated = deterjan_aggregated = sicaklik_aggregated = alt_pompa_aggregated = ust_pompa_aggregated = 0

def calculate():
    global zaman_aggregated, sicaklik_aggregated, deterjan_aggregated, ust_pompa_aggregated, alt_pompa_aggregated
    global zaman_activation, sicaklik_activation, deterjan_activation, ust_pompa_activation, alt_pompa_activation
    global zaman_defuzz, sicaklik_defuzz, deterjan_defuzz, ust_pompa_defuzz, alt_pompa_defuzz
    
    # Define and Apply Rule Base (Kural Tabanı)
    miktar_level_az  = fuzz.interp_membership(x_bulasik_miktar, bulasik_miktar_az, input_miktar)
    miktar_level_ort = fuzz.interp_membership(x_bulasik_miktar, bulasik_miktar_ort, input_miktar)
    miktar_level_cok = fuzz.interp_membership(x_bulasik_miktar, bulasik_miktar_cok, input_miktar)
    kirlilik_level_az  = fuzz.interp_membership(x_kirlilik_derece, kirlilik_derece_az, input_kirlilik)
    kirlilik_level_ort = fuzz.interp_membership(x_kirlilik_derece, kirlilik_derece_ort, input_kirlilik)
    kirlilik_level_cok = fuzz.interp_membership(x_kirlilik_derece, kirlilik_derece_cok, input_kirlilik)
    cins_level_has = fuzz.interp_membership(x_bulasik_cins, bulasik_cins_has, input_cins)
    cins_level_kar = fuzz.interp_membership(x_bulasik_cins, bulasik_cins_kar, input_cins)
    cins_level_guc = fuzz.interp_membership(x_bulasik_cins, bulasik_cins_guc, input_cins)

    # *Kural Tabanı Rule Base
    zaman_activation_ck = zaman_activation_k =  zaman_activation_o =  zaman_activation_u =  zaman_activation_cu = 0
    deterjan_activation_ca =  deterjan_activation_a =  deterjan_activation_n = deterjan_activation_c = deterjan_activation_cf = 0
    sicaklik_activation_dus = sicaklik_activation_nor  = sicaklik_activation_yuk = 0
    alt_pompa_activation_cd =  alt_pompa_activation_d =  alt_pompa_activation_o = alt_pompa_activation_y = alt_pompa_activation_cy = 0
    ust_pompa_activation_cd =  ust_pompa_activation_d =  ust_pompa_activation_o = ust_pompa_activation_y = ust_pompa_activation_cy = 0

    """
    Eğer bulaşık miktarı az ve kirlilik derecesi az kirli ve bulaşık cinsi hassas (kırılabilir) ise
    yıkama zamanı çok kısa ve deterjan miktarı çok az ve su sıcaklığı düşük ve üst
    pompa devri çok düşük ve alt pompa devri çok düşük.
    IF (miktar-az & kirlilik-az & cins-has) THEN zaman-ck, deterjan-ca, sıcaklık-d, ust-pompa-cd, alt-pompa-cd
    """
    rule1 = np.fmin(miktar_level_az, np.fmin(kirlilik_level_az, cins_level_has))
    zaman_activation_ck = np.fmin(rule1, yikama_zaman_ck)
    deterjan_activation_ca = np.fmax(deterjan_activation_ca, np.fmin(rule1, deterjan_miktar_ca))
    sicaklik_activation_dus = np.fmax(sicaklik_activation_dus, np.fmin(rule1, su_sicaklik_dus))
    ust_pompa_activation_cd = np.fmax(ust_pompa_activation_cd, np.fmin(rule1, ust_pompa_cd))
    alt_pompa_activation_cd = np.fmax(alt_pompa_activation_cd, np.fmin(rule1, alt_pompa_cd))
    """
    Eğer bulaşık miktarı az ve kirlilik derecesi çok kirli ve bulaşık cinsi karma ise
    yıkama zamanı orta ve deterjan miktarı normal ve
    su sıcaklığı yüksek ve üst pompa devri düşük ve alt pompa devri çok yüksek.
    IF (miktar-az & kirlilik-cok-kirli & cins-karma) THEN zaman-o, deterjan-n, sıcaklık-y, ust-pompa-d, alt-pompa-cyü
    """
    rule2 = np.fmin(miktar_level_az, np.fmin(kirlilik_level_cok, cins_level_kar))
    zaman_activation_o = np.fmax(zaman_activation_o, np.fmax(zaman_activation_o, np.fmin(rule2, yikama_zaman_o)))
    deterjan_activation_n = np.fmax(deterjan_activation_n, np.fmin(rule2, deterjan_miktar_n))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule2, su_sicaklik_yuk))
    ust_pompa_activation_d = np.fmax(ust_pompa_activation_d, np.fmin(rule2, ust_pompa_d))
    alt_pompa_activation_cy = np.fmax(alt_pompa_activation_cy, np.fmin(rule2, alt_pompa_cy))
    """
    Eğer bulaşık miktarı orta ve kirlilik derecesi orta kirli ve bulaşık cinsi güçlü (sağlam, dayanıklı) ise
    yıkama zamanı orta ve deterjan miktarı normal ve
    su sıcaklığı normal ve üst pompa devri yüksek ve alt pompa devri yüksek.
    IF (miktar-o & kirlilik-o & cins-guc) THEN zaman-o, deterjan-n, sıcaklık-n, ust-pompa-y, alt-pompa-yü
    """
    rule3 = np.fmin(miktar_level_ort, np.fmin(kirlilik_level_ort, cins_level_guc))
    zaman_activation_o = np.fmax(zaman_activation_o, np.fmin(rule3, yikama_zaman_o))
    deterjan_activation_n = np.fmax(deterjan_activation_n, np.fmin(rule3, deterjan_miktar_n))
    sicaklik_activation_nor = np.fmax(sicaklik_activation_nor, np.fmin(rule3, su_sicaklik_nor))
    ust_pompa_activation_y = np.fmax(ust_pompa_activation_y, np.fmin(rule3, ust_pompa_y))
    alt_pompa_activation_y = np.fmax(alt_pompa_activation_y, np.fmin(rule3, alt_pompa_y))
    """
    Eğer bulaşık miktarı çok ve kirlilik derecesi çok kirli ve bulaşık cinsi karma ise
    yıkama zamanı çok uzun ve deterjan miktarı çok fazla ve
    su sıcaklığı yüksek ve üst pompa devri düşük ve alt pompa devri çok yüksek.
    IF (miktar-cok & kirlilik-ck & cins-karma) THEN zaman-cu, deterjan-cf, sıcaklık-y, ust-pompa-d, alt-pompa-cyü
    """
    rule4 = np.fmin(miktar_level_cok, np.fmin(kirlilik_level_cok, cins_level_kar))
    zaman_activation_cu = np.fmax(zaman_activation_cu, np.fmin(rule4, yikama_zaman_cu))
    deterjan_activation_cf = np.fmax(deterjan_activation_cf, np.fmin(rule4, deterjan_miktar_cf))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule4, su_sicaklik_yuk))
    ust_pompa_activation_d = np.fmax(ust_pompa_activation_d, np.fmin(rule4, ust_pompa_d))
    alt_pompa_activation_cy = np.fmax(alt_pompa_activation_cy, np.fmin(rule4, alt_pompa_cy))
    """
    IF (miktar-cok & kirlilik-c & cins-guc) THEN zaman-cu, deterjan-cf, sıcaklık-y, ust-pompa-cy, alt-pompa-cy
    """
    rule5 = np.fmin(miktar_level_cok, np.fmin(kirlilik_level_cok, cins_level_guc))
    zaman_activation_cu = np.fmax(zaman_activation_cu, np.fmin(rule5, yikama_zaman_cu))
    deterjan_activation_cf = np.fmax(deterjan_activation_cf, np.fmin(rule5, deterjan_miktar_cf))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule5, su_sicaklik_yuk))
    ust_pompa_activation_cy = np.fmax(ust_pompa_activation_cy, np.fmin(rule5, ust_pompa_cy))
    alt_pompa_activation_cy = np.fmax(alt_pompa_activation_cy, np.fmin(rule5, alt_pompa_cy))

    """
    IF (miktar-cok & kirlilik-c & cins-has) THEN zaman-cu, deterjan-cf, sıcaklık-y, ust-pompa-cd, alt-pompa-d
    """
    rule6 = np.fmin(miktar_level_cok, np.fmin(kirlilik_level_cok, cins_level_has))
    zaman_activation_cu     = np.fmax(zaman_activation_cu, np.fmin(rule6, yikama_zaman_cu))
    deterjan_activation_cf  = np.fmax(deterjan_activation_cf, np.fmin(rule6, deterjan_miktar_cf))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule6, su_sicaklik_yuk))
    ust_pompa_activation_cd = np.fmax(ust_pompa_activation_cd, np.fmin(rule6, ust_pompa_cd))
    alt_pompa_activation_d  = np.fmax(alt_pompa_activation_d, np.fmin(rule6, alt_pompa_d))

    """
    IF (miktar-orta & kirlilik-a ) THEN zaman-k, deterjan-a, sıcaklık-d, ust-pompa-cd, alt-pompa-d
    """
    rule7 = np.fmin(miktar_level_ort, kirlilik_level_az)
    zaman_activation_k     = np.fmax(zaman_activation_k, np.fmin(rule7, yikama_zaman_k))
    deterjan_activation_a  = np.fmax(deterjan_activation_a, np.fmin(rule7, deterjan_miktar_a))
    sicaklik_activation_dus = np.fmax(sicaklik_activation_dus, np.fmin(rule7, su_sicaklik_dus))
    ust_pompa_activation_cd = np.fmax(ust_pompa_activation_cd, np.fmin(rule7, ust_pompa_cd))
    alt_pompa_activation_d  = np.fmax(alt_pompa_activation_d, np.fmin(rule7, alt_pompa_d))

    """
    IF (miktar-orta & kirlilik-c & (cins-has | cins-kar)) THEN zaman-u, deterjan-f, sıcaklık-y, ust-pompa-d, alt-pompa-y
    """
    rule8 = np.fmin(miktar_level_ort, np.fmin(kirlilik_level_cok, np.fmax(cins_level_has, cins_level_kar)))
    zaman_activation_u     = np.fmax(zaman_activation_u, np.fmin(rule8, yikama_zaman_u))
    deterjan_activation_c  = np.fmax(deterjan_activation_c, np.fmin(rule8, deterjan_miktar_c))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule8, su_sicaklik_yuk))
    ust_pompa_activation_d = np.fmax(ust_pompa_activation_d, np.fmin(rule8, ust_pompa_d))
    alt_pompa_activation_y  = np.fmax(alt_pompa_activation_y, np.fmin(rule8, alt_pompa_y))

    """
    IF (miktar-orta & kirlilik-c & cins-guc) THEN zaman-u, deterjan-f, sıcaklık-y, ust-pompa-y, alt-pompa-cy
    """
    rule9 = np.fmin(miktar_level_ort, np.fmin(kirlilik_level_cok, cins_level_guc))
    zaman_activation_u     = np.fmax(zaman_activation_u, np.fmin(rule9, yikama_zaman_u))
    deterjan_activation_c  = np.fmax(deterjan_activation_c, np.fmin(rule9, deterjan_miktar_c))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule9, su_sicaklik_yuk))
    ust_pompa_activation_y = np.fmax(ust_pompa_activation_y, np.fmin(rule9, ust_pompa_y))
    alt_pompa_activation_cy  = np.fmax(alt_pompa_activation_cy, np.fmin(rule9, alt_pompa_cy))

    """
    IF (miktar-orta & kirlilik-o & (cins_has | cins-kar)) THEN zaman-o, deterjan-n, sıcaklık-n, ust-pompa-d, alt-pompa-o
    """
    rule10 = np.fmin(miktar_level_ort, np.fmin(kirlilik_level_ort, np.fmax(cins_level_has, cins_level_kar)))
    zaman_activation_o     = np.fmax(zaman_activation_o, np.fmin(rule10, yikama_zaman_o))
    deterjan_activation_n  = np.fmax(deterjan_activation_n, np.fmin(rule10, deterjan_miktar_n))
    sicaklik_activation_nor = np.fmax(sicaklik_activation_nor, np.fmin(rule10, su_sicaklik_nor))
    ust_pompa_activation_d = np.fmax(ust_pompa_activation_d, np.fmin(rule10, ust_pompa_d))
    alt_pompa_activation_o  = np.fmax(alt_pompa_activation_o, np.fmin(rule10, alt_pompa_o))

    """
    IF (miktar-cok & kirlilik-o ) THEN zaman-u, deterjan-f, sıcaklık-n, ust-pompa-d, alt-pompa-o
    """
    rule11 = np.fmin(miktar_level_cok, kirlilik_level_ort)
    zaman_activation_u      = np.fmax(zaman_activation_u, np.fmin(rule11, yikama_zaman_u))
    deterjan_activation_c   = np.fmax(deterjan_activation_c, np.fmin(rule11, deterjan_miktar_c))
    sicaklik_activation_nor = np.fmax(sicaklik_activation_nor, np.fmin(rule11, su_sicaklik_nor))
    ust_pompa_activation_d  = np.fmax(ust_pompa_activation_d, np.fmin(rule11, ust_pompa_d))
    alt_pompa_activation_o  = np.fmax(alt_pompa_activation_o, np.fmin(rule11, alt_pompa_o))

    """
    IF (miktar-cok & kirlilik-a ) THEN zaman-o, deterjan-n, sıcaklık-d, ust-pompa-d, alt-pompa-cd
    """
    rule12 = np.fmin(miktar_level_cok, kirlilik_level_az)
    zaman_activation_o     =  np.fmax(zaman_activation_o, np.fmin(rule12, yikama_zaman_o))
    deterjan_activation_n  =  np.fmax(deterjan_activation_n, np.fmin(rule12, deterjan_miktar_n))
    sicaklik_activation_dus = np.fmax(sicaklik_activation_dus, np.fmin(rule12, su_sicaklik_dus))
    ust_pompa_activation_d =  np.fmax(ust_pompa_activation_d, np.fmin(rule12, ust_pompa_d))
    alt_pompa_activation_cd = np.fmax(alt_pompa_activation_cd, np.fmin(rule12, alt_pompa_cd))

    """
    IF (miktar-az & kirlilik-a & (cins_kar | cins-guc)) THEN zaman-ck, deterjan-ca, sıcaklık-d, ust-pompa-d, alt-pompa-cd
    """
    rule13 = np.fmin(miktar_level_az, np.fmin(kirlilik_level_az, np.fmax(cins_level_kar, cins_level_guc)))
    zaman_activation_ck =     np.fmax(zaman_activation_ck, np.fmin(rule13, yikama_zaman_ck))
    deterjan_activation_ca =  np.fmax(deterjan_activation_ca, np.fmin(rule13, deterjan_miktar_ca))
    sicaklik_activation_dus = np.fmax(sicaklik_activation_dus, np.fmin(rule13, su_sicaklik_dus))
    ust_pompa_activation_d =  np.fmax(ust_pompa_activation_d, np.fmin(rule13, ust_pompa_d))
    alt_pompa_activation_cd = np.fmax(alt_pompa_activation_cd, np.fmin(rule13, alt_pompa_cd))

    """
    IF (miktar-az & kirlilik-c & cins-has) THEN zaman-o, deterjan-n, sıcaklık-y, ust-pompa-d, alt-pompa-y
    """
    rule14 = np.fmin(miktar_level_az, np.fmin(kirlilik_level_cok, cins_level_has))
    zaman_activation_o =      np.fmax(zaman_activation_o, np.fmin(rule14, yikama_zaman_o))
    deterjan_activation_n =   np.fmax(deterjan_activation_n, np.fmin(rule14, deterjan_miktar_n))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule14, su_sicaklik_yuk))
    ust_pompa_activation_d =  np.fmax(ust_pompa_activation_d, np.fmin(rule14, ust_pompa_d))
    alt_pompa_activation_y =  np.fmax(alt_pompa_activation_y, np.fmin(rule14, alt_pompa_y))

    """
    IF (miktar-az & kirlilik-c & cins-guc) THEN zaman-o, deterjan-n, sıcaklık-y, ust-pompa-o, alt-pompa-cy
    """
    rule15 = np.fmin(miktar_level_az, np.fmin(kirlilik_level_cok, cins_level_guc))
    zaman_activation_o =      np.fmax(zaman_activation_o, np.fmin(rule15, yikama_zaman_o))
    deterjan_activation_n =   np.fmax(deterjan_activation_n, np.fmin(rule15, deterjan_miktar_n))
    sicaklik_activation_yuk = np.fmax(sicaklik_activation_yuk, np.fmin(rule15, su_sicaklik_yuk))
    ust_pompa_activation_o =  np.fmax(ust_pompa_activation_o, np.fmin(rule15, ust_pompa_o))
    alt_pompa_activation_cy = np.fmax(alt_pompa_activation_cy, np.fmin(rule15, alt_pompa_cy))

    """
    IF (miktar-az & kirlilik-o) THEN zaman-k, deterjan-az, sıcaklık-n, ust-pompa-d, alt-pompa-o
    """
    rule16 = np.fmin(miktar_level_az, kirlilik_level_ort)
    zaman_activation_k =      np.fmax(zaman_activation_k, np.fmin(rule16, yikama_zaman_k))
    deterjan_activation_a =   np.fmax(deterjan_activation_a, np.fmin(rule16, deterjan_miktar_a))
    sicaklik_activation_nor = np.fmax(sicaklik_activation_nor, np.fmin(rule16, su_sicaklik_nor))
    ust_pompa_activation_d =  np.fmax(ust_pompa_activation_d, np.fmin(rule16, ust_pompa_d))
    alt_pompa_activation_o =  np.fmax(alt_pompa_activation_o, np.fmin(rule16, alt_pompa_o))


    # *Aggregation ve Defuzzification
    zaman_aggregated = np.fmax(zaman_activation_ck, np.fmax(zaman_activation_k, np.fmax(zaman_activation_o, np.fmax(zaman_activation_u, zaman_activation_cu))))
    zaman_defuzz = fuzz.defuzz(yikama_zaman, zaman_aggregated, 'centroid')                  # crips
    zaman_activation = fuzz.interp_membership(yikama_zaman, zaman_aggregated, zaman_defuzz) # membership value
    
    deterjan_aggregated = np.fmax(deterjan_activation_ca, np.fmax(deterjan_activation_a, np.fmax(deterjan_activation_n,np.fmax(deterjan_activation_c, deterjan_activation_cf))))
    deterjan_defuzz = fuzz.defuzz(deterjan_miktar, deterjan_aggregated, 'centroid')                     # crips
    deterjan_activation = fuzz.interp_membership(deterjan_miktar, deterjan_aggregated, deterjan_defuzz) # membership value
    
    sicaklik_aggregated = np.fmax(sicaklik_activation_dus, np.fmax(sicaklik_activation_nor, sicaklik_activation_yuk))
    sicaklik_defuzz = fuzz.defuzz(su_sicaklik, sicaklik_aggregated, 'centroid')                     # crips
    sicaklik_activation = fuzz.interp_membership(su_sicaklik, sicaklik_aggregated, sicaklik_defuzz) # membership value
    
    alt_pompa_aggregated = np.fmax(alt_pompa_activation_cd, np.fmax(alt_pompa_activation_d ,np.fmax(alt_pompa_activation_o, np.fmax(alt_pompa_activation_y ,alt_pompa_activation_cy))))
    alt_pompa_defuzz = fuzz.defuzz(alt_pompa, alt_pompa_aggregated, 'centroid')                      # crips
    alt_pompa_activation = fuzz.interp_membership(alt_pompa, alt_pompa_aggregated, alt_pompa_defuzz) # membership value
    
    ust_pompa_aggregated = np.fmax(ust_pompa_activation_cd, np.fmax(ust_pompa_activation_d, np.fmax(ust_pompa_activation_o, np.fmax(ust_pompa_activation_y, ust_pompa_activation_cy))))
    ust_pompa_defuzz = fuzz.defuzz(ust_pompa, ust_pompa_aggregated, 'centroid')                      # crips
    ust_pompa_activation = fuzz.interp_membership(ust_pompa, ust_pompa_aggregated, ust_pompa_defuzz) # membership value


# *Input Plot
def input_plot() :
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

    ax0.plot(x_bulasik_miktar, bulasik_miktar_az,  'b', linewidth = 1.5, label = "az")
    ax0.plot(x_bulasik_miktar, bulasik_miktar_ort, 'g', linewidth = 1.5, label = "orta")
    ax0.plot(x_bulasik_miktar, bulasik_miktar_cok, 'r', linewidth = 1.5, label = "çok")
    ax0.set_title("Bulaşık Miktarı")
    ax0.legend()

    ax1.plot(x_kirlilik_derece, kirlilik_derece_az,  'b', linewidth = 1.5, label = "Az Kirli")
    ax1.plot(x_kirlilik_derece, kirlilik_derece_ort, 'g', linewidth = 1.5, label = "Orta Kirli")
    ax1.plot(x_kirlilik_derece, kirlilik_derece_cok, 'r', linewidth = 1.5, label = "Çok Kirli")
    ax1.set_title("Kirlilik derecesi")
    ax1.legend()

    ax2.plot(x_bulasik_cins, bulasik_cins_has, 'b', linewidth= 1.5, label = "Hassas")
    ax2.plot(x_bulasik_cins, bulasik_cins_kar, 'g', linewidth= 1.5, label = "Karma")
    ax2.plot(x_bulasik_cins, bulasik_cins_guc, 'r', linewidth= 1.5, label = "Güçlü")
    ax2.set_title("Bulaşık Cinsi")
    ax2.legend()
    
    plt.tight_layout()
    plt.show()



# *Output Plot
def output_plot() :
    fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(8, 9))

    ax0.plot(yikama_zaman, yikama_zaman_ck, 'b', linewidth = 1.5, label = "Çok Kısa")
    ax0.plot(yikama_zaman, yikama_zaman_k,  'g', linewidth = 1.5, label = "Kısa")
    ax0.plot(yikama_zaman, yikama_zaman_o,  'r', linewidth = 1.5, label = "Orta")
    ax0.plot(yikama_zaman, yikama_zaman_u,  'y', linewidth = 1.5, label = "Uzun")
    ax0.plot(yikama_zaman, yikama_zaman_cu, 'y', linewidth = 1.5, label = "Çok Uzun")
    ax0.set_title("Yıkama Zamanı")
    ax0.legend()

    ax1.plot(deterjan_miktar, deterjan_miktar_ca, 'b', linewidth = 1.5, label = "Çok Az")
    ax1.plot(deterjan_miktar, deterjan_miktar_a,  'b', linewidth = 1.5, label = "Az")
    ax1.plot(deterjan_miktar, deterjan_miktar_n,  'y', linewidth = 1.5, label = "Normal")
    ax1.plot(deterjan_miktar, deterjan_miktar_c,  'g', linewidth = 1.5, label = "Çok")
    ax1.plot(deterjan_miktar, deterjan_miktar_cf, 'r', linewidth = 1.5, label = "Çok Fazla")
    ax1.set_title("Deterjan Miktarı")
    ax1.legend()

    ax2.plot(su_sicaklik, su_sicaklik_dus, 'b', linewidth= 1.5, label = "Düşük")
    ax2.plot(su_sicaklik, su_sicaklik_nor, 'g', linewidth= 1.5, label = "Normal")
    ax2.plot(su_sicaklik, su_sicaklik_yuk, 'r', linewidth= 1.5, label = "Yüksek")
    ax2.set_title("Su Sıcaklığı")
    ax2.legend()

    ax3.plot(ust_pompa, ust_pompa_cd, 'b', linewidth= 1.5, label = "Çok Düşük")
    ax3.plot(ust_pompa, ust_pompa_d,  'b', linewidth= 1.5, label = "Normal")
    ax3.plot(ust_pompa, ust_pompa_o,  'g', linewidth= 1.5, label = "Orta")
    ax3.plot(ust_pompa, ust_pompa_y,  'r', linewidth= 1.5, label = "Yüksek")
    ax3.plot(ust_pompa, ust_pompa_cy, 'r', linewidth= 1.5, label = "Çok Yüksek")
    ax3.set_title("Üst Pompa Devri")
    ax3.legend()

    ax4.plot(alt_pompa, alt_pompa_cd, 'b', linewidth= 1.5, label = "Çok Düşük")
    ax4.plot(alt_pompa, alt_pompa_d,  'b', linewidth= 1.5, label = "Normal")
    ax4.plot(alt_pompa, alt_pompa_o,  'g', linewidth= 1.5, label = "Orta")
    ax4.plot(alt_pompa, alt_pompa_y,  'r', linewidth= 1.5, label = "Yüksek")
    ax4.plot(alt_pompa, alt_pompa_cy, 'r', linewidth= 1.5, label = "Çok Yüksek")
    ax4.set_title("Alt Pompa Devri")
    ax4.legend()

    plt.tight_layout()
    plt.show()

def show_result_plot():
    fig, (ax0, ax1, ax2, ax3, ax4)  = plt.subplots(nrows=5, figsize=(8, 9))
    
    ax0.plot(yikama_zaman, yikama_zaman_ck, 'b', linewidth=1.5, linestyle=':', label = "Çok Kısa")
    ax0.plot(yikama_zaman, yikama_zaman_k,  'b', linewidth=1.5, linestyle=':', label = "Kısa")
    ax0.plot(yikama_zaman, yikama_zaman_o,  'g', linewidth=1.5, linestyle=':', label = "Orta")
    ax0.plot(yikama_zaman, yikama_zaman_u,  'r', linewidth=1.5, linestyle=':', label = "Uzun")
    ax0.plot(yikama_zaman, yikama_zaman_cu, 'r', linewidth=1.5, linestyle=':', label = "Çok Uzun")
    ax0.fill_between(yikama_zaman, np.zeros_like(yikama_zaman), zaman_aggregated, facecolor='Orange', alpha=0.7)
    ax0.plot([zaman_defuzz, zaman_defuzz], [0, zaman_activation], 'k', linewidth=1.5, alpha=0.9)
    ax0.set_title('Yıkama Zamanı')
    ax0.legend()

    ax1.plot(deterjan_miktar, deterjan_miktar_ca, 'b', linewidth = 1.5, linestyle=':', label = "Çok Az")
    ax1.plot(deterjan_miktar, deterjan_miktar_a,  'b', linewidth = 1.5, linestyle=':', label = "Az")
    ax1.plot(deterjan_miktar, deterjan_miktar_n,  'y', linewidth = 1.5, linestyle=':', label = "Normal")
    ax1.plot(deterjan_miktar, deterjan_miktar_c,  'g', linewidth = 1.5, linestyle=':', label = "Çok")
    ax1.plot(deterjan_miktar, deterjan_miktar_cf, 'r', linewidth = 1.5, linestyle=':', label = "Çok Fazla")
    ax1.fill_between(deterjan_miktar, np.zeros_like(deterjan_miktar), deterjan_aggregated, facecolor='Orange', alpha=0.7)
    ax1.plot([deterjan_defuzz, deterjan_defuzz], [0, deterjan_activation], 'k', linewidth=1.5, alpha=0.9)
    ax1.set_title("Deterjan Miktarı")
    ax1.legend()
 
    ax2.plot(su_sicaklik, su_sicaklik_dus, 'b', linewidth= 1.5, linestyle=':', label = "Düşük")
    ax2.plot(su_sicaklik, su_sicaklik_nor, 'g', linewidth= 1.5, linestyle=':', label = "Normal")
    ax2.plot(su_sicaklik, su_sicaklik_yuk, 'r', linewidth= 1.5, linestyle=':', label = "Yüksek")
    ax2.fill_between(su_sicaklik, np.zeros_like(su_sicaklik), sicaklik_aggregated, facecolor='Orange', alpha=0.7)
    ax2.plot([sicaklik_defuzz, sicaklik_defuzz], [0, sicaklik_activation], 'k', linewidth=1.5, alpha=0.9)
    ax2.set_title("Su Sıcaklığı")
    ax2.legend()

    ax3.plot(ust_pompa, ust_pompa_cd, 'b', linewidth= 1.5, linestyle=':', label = "Çok Düşük")
    ax3.plot(ust_pompa, ust_pompa_d,  'b', linewidth= 1.5, linestyle=':', label = "Düşük")
    ax3.plot(ust_pompa, ust_pompa_o,  'g', linewidth= 1.5, linestyle=':', label = "Orta")
    ax3.plot(ust_pompa, ust_pompa_y,  'r', linewidth= 1.5, linestyle=':', label = "Yüksek")
    ax3.plot(ust_pompa, ust_pompa_cy, 'r', linewidth= 1.5, linestyle=':', label = "Çok Yüksek")
    ax3.fill_between(ust_pompa, np.zeros_like(ust_pompa), ust_pompa_aggregated, facecolor='Orange', alpha=0.7)
    ax3.plot([ust_pompa_defuzz, ust_pompa_defuzz], [0, ust_pompa_activation], 'k', linewidth=1.5, alpha=0.9)
    ax3.set_title("Üst Pompa Devri")
    ax3.legend()

    ax4.plot(alt_pompa, alt_pompa_cd, 'b', linewidth= 1.5, linestyle=':', label = "Çok Düşük")
    ax4.plot(alt_pompa, alt_pompa_d,  'b', linewidth= 1.5, linestyle=':', label = "Düşük")
    ax4.plot(alt_pompa, alt_pompa_o,  'g', linewidth= 1.5, linestyle=':', label = "Orta")
    ax4.plot(alt_pompa, alt_pompa_y,  'r', linewidth= 1.5, linestyle=':', label = "Yüksek")
    ax4.plot(alt_pompa, alt_pompa_cy, 'r', linewidth= 1.5, linestyle=':', label = "Çok Yüksek")
    ax4.set_title("Alt Pompa Devri")
    ax4.fill_between(alt_pompa, np.zeros_like(alt_pompa), alt_pompa_aggregated, facecolor='Orange', alpha=0.7)
    ax4.plot([alt_pompa_defuzz, alt_pompa_defuzz], [0, alt_pompa_activation], 'k', linewidth=1.5, alpha=0.9)
    ax4.legend()

    plt.tight_layout()
    plt.show()

def show_result_3d():
    global input_kirlilik, input_miktar, input_cins
    unsampled = np.linspace(0, 100, 10)
    sim_x, sim_y = np.meshgrid(unsampled, unsampled)
    zaman = np.zeros_like(sim_x)
    deterjan = np.zeros_like(sim_x)
    sicaklik = np.zeros_like(sim_x)
    alt= np.zeros_like(sim_x)
    ust = np.zeros_like(sim_x)

    for i in range(10):
        for j in range(10):
            input_miktar = sim_x[i, j]
            input_kirlilik = sim_y[i, j]
            input_cins = 50
            calculate()
            zaman[i, j] = zaman_defuzz
            deterjan[i, j] = deterjan_defuzz
            sicaklik[i, j] = sicaklik_defuzz

    # *Zaman
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('Miktar', fontsize=15)
    ax.set_ylabel('Kirlilik', fontsize=15)
    ax.set_zlabel('Zaman', fontsize=15)

    surf = ax.plot_surface(sim_x, sim_y, zaman, rstride=1, cstride=1, cmap='viridis',
                        linewidth=0.4, antialiased=True)

    cset = ax.contourf(sim_x, sim_y, zaman, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, zaman, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, zaman, zdir='y', offset=3, cmap='viridis', alpha=0.5)

    ax.view_init(30, 200)

    # *Deterjan
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('Miktar', fontsize=15)
    ax.set_ylabel('Kirlilik', fontsize=15)
    ax.set_zlabel('Deterjan Miktarı', fontsize=15)

    surf = ax.plot_surface(sim_x, sim_y, deterjan, rstride=1, cstride=1, cmap='viridis',
                        linewidth=0.4, antialiased=True)

    cset = ax.contourf(sim_x, sim_y, deterjan, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, deterjan, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, deterjan, zdir='y', offset=3, cmap='viridis', alpha=0.5)

    ax.view_init(30, 200)

    # *Sıcaklık
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('Miktar', fontsize=15)
    ax.set_ylabel('Kirlilik', fontsize=15)
    ax.set_zlabel('Sıcaklık', fontsize=15)

    surf = ax.plot_surface(sim_x, sim_y, sicaklik, rstride=1, cstride=1, cmap='viridis',
                        linewidth=0.4, antialiased=True)

    cset = ax.contourf(sim_x, sim_y, sicaklik, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, sicaklik, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, sicaklik, zdir='y', offset=3, cmap='viridis', alpha=0.5)

    ax.view_init(30, 200)

    for i in range(10):
        for j in range(10):
            input_cins = sim_x[i, j]
            input_kirlilik = sim_y[i, j]
            input_miktar = 50
            calculate()
            alt[i, j] = alt_pompa_defuzz
            ust[i, j] = ust_pompa_defuzz

    # *Alt Pompa
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('Dayanıklılık', fontsize=15)
    ax.set_ylabel('Kirlilik', fontsize=15)
    ax.set_zlabel('Alt Pompa', fontsize=15)

    surf = ax.plot_surface(sim_x, sim_y, alt, rstride=1, cstride=1, cmap='viridis',
                        linewidth=0.4, antialiased=True)

    cset = ax.contourf(sim_x, sim_y, alt, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, alt, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, alt, zdir='y', offset=3, cmap='viridis', alpha=0.5)
    
    # *Üst Pompa
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('Dayanıklılık', fontsize=15)
    ax.set_ylabel('Kirlilik', fontsize=15)
    ax.set_zlabel('Üst Pompa', fontsize=15)

    surf = ax.plot_surface(sim_x, sim_y, ust, rstride=1, cstride=1, cmap='viridis',
                        linewidth=0.4, antialiased=True)

    cset = ax.contourf(sim_x, sim_y, ust, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, ust, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, ust, zdir='y', offset=3, cmap='viridis', alpha=0.5)
    

    plt.show()


#output_plot()
#show_result_plot()
#show_result_3d()
"""
def oshow_result_3d():
    global input_kirlilik, input_miktar, input_cins
    unsampled = np.linspace(0, 100, 10)
    sim_x, sim_y = np.meshgrid(unsampled, unsampled)
    sim_z = np.zeros_like(sim_x)
    for i in range(10):
        for j in range(10):
            input_cins = sim_x[i, j]
            input_kirlilik = sim_y[i, j]
            calculate()
            sim_z[i, j] = ust_pompa_defuzz

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('Dayanıklılık', fontsize=15)
    ax.set_ylabel('Kirlilik', fontsize=15)
    ax.set_zlabel('Deterjan Miktarı', fontsize=15)

    surf = ax.plot_surface(sim_x, sim_y, sim_z, rstride=1, cstride=1, cmap='viridis',
                        linewidth=0.4, antialiased=True)

    cset = ax.contourf(sim_x, sim_y, sim_z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, sim_z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
    cset = ax.contourf(sim_x, sim_y, sim_z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

    ax.view_init(30, 200)
    plt.show()
"""