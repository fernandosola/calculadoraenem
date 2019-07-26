from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import render
import numpy as np


def index(request):
    return render(request, 'calculadora/index.html')


def calcular(request):

    dicionario = {float(641.27673163999998): [540.38, 624.06, 673.49, 727.5200000000001],
            float(516.57467515999997): [435.46000000000004, 498.14, 541.94, 599.0600000000001],
            float(517.01045523000005): [441.2, 502.73999999999995, 545.04, 600.24],
            float(523.08916180000006): [440.2, 508.91999999999996, 550.9200000000001, 605.3499999999999],
            float(525.49949729000002): [447.6, 512.5799999999999, 556.74, 610.72],
            float(527.11130793999996): [451.58000000000004, 510.54, 552.5200000000001, 607.3199999999999],
            float(534.90021823999996): [461.53000000000003, 512.49, 555.29, 614.5600000000001],
            float(540.44152155999996): [451.4, 517.82, 568.75, 631.29],
            float(423.12715790999999): [331.64, 419.03999999999996, 457.81, 502.64],
            float(560.50749273999998): [480.45000000000005, 544.5, 590.12, 643.3799999999999],
            float(560.01308187999996): [483.40999999999997, 540.0, 586.2, 642.8],
            float(563.73081757): [487.01, 550.4399999999999, 594.9499999999999, 658.0200000000001],
            float(436.19262837000002): [337.49, 432.6500000000001, 470.5, 519.9],
            float(566.91668786000002): [488.97, 549.08, 593.72, 650.55],
            float(442.58399505): [337.21999999999997, 433.46000000000004, 471.56000000000006, 521.74],
            float(445.19263531000001): [343.49, 439.31, 478.71, 527.12],
            float(580.49245071999997): [499.65999999999997, 561.48, 606.08, 662.28],
            float(456.41848490000001): [370.57000000000005, 447.5, 484.88, 535.76],
            float(460.34310856000002): [357.15999999999997, 450.7, 491.68, 547.1200000000001],
            float(467.62819468999999): [357.32000000000005, 461.76000000000005, 506.64, 556.56],
            float(596.70062638000002): [511.8, 575.38, 621.96, 677.9399999999999],
            float(597.61829293999995): [510.06000000000006, 579.03, 627.04, 683.28],
            float(469.94575800000001): [399.74, 456.4, 494.56000000000006, 547.62],
            float(471.72499683000001): [390.54, 462.65, 501.7, 554.52], 596.50828320999995: [510.32, 573.31, 622.34, 684.62],
            float(479.27696907000001): [406.97999999999996, 469.48, 506.76000000000005, 558.29],
            float(607.99400586000002): [524.1700000000001, 590.86, 636.6600000000001, 693.92],
            float(481.88560339999998): [350.86, 460.88, 505.14, 560.34],
            float(482.86000360000003): [414.36, 473.78000000000003, 511.66, 568.34],
            float(488.47530066000002): [413.52000000000004, 474.75999999999993, 514.1, 569.71],
            float(489.00325129999999): [415.21, 474.7, 519.0, 576.04], 489.42353711999999: [420.16, 475.57, 520.13, 573.66],
            float(491.14006705999998): [399.27000000000004, 478.15999999999997, 518.45, 566.7],
            float(492.07538658999999): [412.39000000000004, 478.11, 525.51, 585.05],
            float(622.67419113999995): [531.6, 602.8399999999999, 648.08, 706.26],
            float(497.78957744000002): [424.03999999999996, 486.78, 525.19, 585.25],
            float(499.45870957): [430.18, 487.42, 526.19, 576.9],
            float(628.57238843000005): [540.7, 614.6800000000001, 664.1800000000001, 717.36],
            float(501.00095577000002): [424.8, 484.21999999999997, 527.2, 586.02],
            float(508.92750432999998): [437.83, 494.4200000000001, 535.1200000000001, 587.9]};

    renda_per_capita_1 = np.float64(request.GET["renda_per_capita_1"])
    renda_per_capita_2 = np.float64(request.GET["renda_per_capita_2"])
    renda_per_capita = renda_per_capita_1 / renda_per_capita_2
    ind_esc_pub_e_m = np.float64(request.GET["ind_esc_pub_e_m"])
    Q024_A = np.float64(request.GET["Q024_A"])
    NU_IDADE = np.float64(request.GET["NU_IDADE"])
    Q025_A = np.float64(request.GET["Q025_A"])
    Q013_A = np.float64(request.GET["Q013_A"])
    Q007_A = np.float64(request.GET["Q007_A"])
    NU_EQUIP_MULTIMIDIA_por_aluno_classe_quartil = np.float64(request.GET["NU_EQUIP_MULTIMIDIA_por_aluno_classe_quartil"])
    Q023_A = np.float64(request.GET["Q023_A"])
    TP_DEPENDENCIA_ADM_ESC_x_4 = np.float64(request.GET["TP_DEPENDENCIA_ADM_ESC_x_4"])
    Q004_E = np.float64(request.GET["Q004_E"])
    Q004_D = np.float64(request.GET["Q004_D"])
    Q003_A = np.float64(request.GET["Q003_A"])
    Q003_D = np.float64(request.GET["Q003_D"])
    Q003_E = np.float64(request.GET["Q003_E"])
    Q022_B = np.float64(request.GET["Q022_B"])
    num_alunos_por_SALA_classe_quartil = np.float64(request.GET["num_alunos_por_SALA_classe_quartil"])
    empenho = np.float64(request.GET["empenho"])

    def tree():
        if renda_per_capita <= 562.2015380859375:
            if ind_esc_pub_e_m <= 0.5:
                if renda_per_capita <= 240.41598510742188:
                    if NU_IDADE <= 18.5:
                        if Q024_A <= 0.5:
                            return 560.01308188
                        else:  # if Q024_A > 0.5
                            return 534.90021824
                    else:  # if NU_IDADE > 18.5
                        if TP_DEPENDENCIA_ADM_ESC_x_4 <= 0.5:
                            return 540.44152156
                        else:  # if TP_DEPENDENCIA_ADM_ESC_x_4 > 0.5
                            return 489.42353712
                else:  # if renda_per_capita > 240.41598510742188
                    return 566.91668786
            else:  # if ind_esc_pub_e_m > 0.5
                if NU_IDADE <= 18.5:
                    if Q024_A <= 0.5:
                        if NU_EQUIP_MULTIMIDIA_por_aluno_classe_quartil <= 0.625:
                            if Q004_D <= 0.5:
                                if Q022_B <= 0.5:
                                    if NU_IDADE <= 17.5:
                                        return 499.45870957
                                    else:  # if NU_IDADE > 17.5
                                        return 488.47530066
                                else:  # if Q022_B > 0.5
                                    return 482.8600036
                            else:  # if Q004_D > 0.5
                                return 508.92750433
                        else:  # if NU_EQUIP_MULTIMIDIA_por_aluno_classe_quartil > 0.625
                            if Q023_A <= 0.5:
                                return 516.57467516
                            else:  # if Q023_A > 0.5
                                return 501.00095577
                    else:  # if Q024_A > 0.5
                        if NU_IDADE > 18.5:
                            if renda_per_capita <= 156.16806030273438:
                                return 456.4184849
                            else:  # if renda_per_capita > 156.16806030273438
                                return 471.72499683
                        else:
                            if Q003_A <= 0.5:
                                if Q003_D <= 0.5:
                                    return 479.27696907
                                else:  # if Q003_D > 0.5
                                    return 497.78957744
                            else:  # if Q003_A > 0.5
                                return 469.945758
                else:  # if NU_IDADE > 18.5
                    if Q013_A <= 0.5:
                        if Q024_A <= 0.5:
                            return 460.34310856
                        else:  # if Q024_A > 0.5
                            return 436.19262837
                    else:  # if Q013_A > 0.5
                        if renda_per_capita <= 133.85821533203125:
                            if Q024_A <= 0.5:
                                return 442.58399505
                            else:  # if Q024_A > 0.5
                                return 423.12715791
                        else:  # if renda_per_capita > 133.85821533203125
                            return 445.19263531
        else:  # if renda_per_capita > 562.2015380859375
            if num_alunos_por_SALA_classe_quartil <= 0.625:
                if ind_esc_pub_e_m <= 0.5:
                    if renda_per_capita <= 1940.934326171875:
                        return 596.50828321
                    else:  # if renda_per_capita > 1940.934326171875
                        return 641.27673164
                else:  # if ind_esc_pub_e_m > 0.5
                    if renda_per_capita <= 1087.1614990234375:
                        if Q025_A <= 0.5:
                            if NU_IDADE <= 18.5:
                                if Q004_D <= 0.5:
                                    if Q024_A <= 0.5:
                                        return 517.01045523
                                    else:  # if Q024_A > 0.5
                                        return 491.14006706
                                else:  # if Q004_D > 0.5
                                    return 527.11130794
                            else:  # if NU_IDADE > 18.5
                                return 467.62819469
                        else:  # if Q025_A > 0.5
                            return 489.0032513
                    else:  # if renda_per_capita > 1087.1614990234375
                        if NU_EQUIP_MULTIMIDIA_por_aluno_classe_quartil <= 0.625:
                            return 523.0891618
                        else:  # if NU_EQUIP_MULTIMIDIA_por_aluno_classe_quartil > 0.625
                            return 560.50749274
            else:  # if num_alunos_por_SALA_classe_quartil > 0.625
                if ind_esc_pub_e_m <= 0.5:
                    if Q003_E <= 0.5:
                        if Q007_A <= 0.5:
                            return 607.99400586
                        else:  # if Q007_A > 0.5
                            if Q024_A <= 0.5:
                                if Q003_D <= 0.5:
                                    return 580.49245072
                                else:  # if Q003_D > 0.5
                                    return 596.70062638
                            else:  # if Q024_A > 0.5
                                return 563.73081757
                    else:  # if Q003_E > 0.5
                        if Q004_E <= 0.5:
                            if renda_per_capita <= 2045.040283203125:
                                return 597.61829294
                            else:  # if renda_per_capita > 2045.040283203125
                                return 622.67419114
                        else:  # if Q004_E > 0.5
                            return 628.57238843
                else:  # if ind_esc_pub_e_m > 0.5
                    if Q024_A <= 0.5:
                        if NU_IDADE <= 18.5:
                            return 525.49949729
                        else:  # if NU_IDADE > 18.5
                            return 481.8856034
                    else:  # if Q024_A > 0.5
                        return 492.07538659
    resultado_1 = tree()
    resultado_2 = dicionario[resultado_1][int(empenho - 1)];
    resultado_2 = int(resultado_2 * 100)/100
    resultado_2 = str(resultado_2).replace('.', ',')
    return JsonResponse({'resultado': str(resultado_2)})



