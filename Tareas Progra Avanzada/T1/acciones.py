from cargar_datos import barcos, tripulantes, mercancias
import parametros
from currency_converter import CurrencyConverter
c = CurrencyConverter()


def mostrar_riesgo(canal):
    if len(canal.barcos) > 0:
        print()
        print("**** RIESGO DE ENCALLAMIENTO ****")
        print()

        for barco in canal.barcos:
            print(f"La probabilidad de que {barcos[barco].nombre} encalle es de {barcos[barco].probabilidad_encallar}")
            print()
    else:
        print()
        print("Todavía no hay barcos en el canal")
        print()
    pass
def desencallar_barco(canal):
    print()
    if len(canal.barcos_encallados) > 0: 
        print()
        print("****BARCOS ENCALLADOS****")
        print()
        for barco in canal.barcos:
            if barcos[barco].encallado == True:
                print(f"El barco {barcos[barco].nombre} esta encallado en el kilometro {round(barcos[barco].ubicacion,1)}")
                if barcos[barco].nombre not in canal.barcos_encallados:
                    canal.barcos_encallados.append(barcos[barco].nombre)
        print()    
        barco_a_desencallar = input("¿Que barco desea tratar de desencallar?: ") 
        print()
        if barco_a_desencallar in canal.barcos_encallados:
            canal.desencallar_barco(barcos[barco_a_desencallar])
        else:
            print("El barco que escribio no se encuentra dentro de los barcos encallados")
    else: 
        print()
        print("No hay barcos encallados en este momento")
        print()

    if canal.dinero <= 0:
        print("Se acabaron los fondos del canal, perdiste :(")  
        quit()
    pass
def simular_hora(canal):
    canal.dinero_gastado_hora = 0
    canal.dinero_recibido_hora = 0
    if len(canal.barcos_encallados) == 0:
        print()
        print("Los barcos disponibles para entrar al canal son:")
        print()
        for barco in barcos.keys():
            if barco not in canal.barcos:
                print(barco)
                
        print()
        barco_a_ingresar = input("¿Que barco desea ingresar?: " )
        if barco_a_ingresar not in canal.barcos and barco_a_ingresar in barcos.keys():
            canal.ingresar_barco(barcos[barco_a_ingresar])
            barcos[barco_a_ingresar].desplazarse()
            if barcos[barco_a_ingresar].encallar() == True:
                canal.barcos_encallaron += 1
                canal.barcos_encallados.append(barcos[barco_a_ingresar].nombre)
                print()
                print("Mala suerte, el barco encallo apenas ingresó al canal :/")
                print()
                for tripulante in barcos[barco_a_ingresar].tripulacion:
                    if tripulantes[tripulante].tipo == "DCCapitán":
                        tripulantes[tripulante].desencallar = False
                        barcos[barco_a_ingresar].encallado = False
                        canal.barcos_encallados.remove(barcos[barco_a_ingresar].nombre)
                        print("Menos mal que su capitán los salvo de esta!!")
                        print()
            else:
                print("Hemos ingresado el barco con éxito")
                print()
        else:
            print()
            print("El barco ingresado no existe")
            print()     
        

    
        
    
    for barco_en_canal in canal.barcos:
        if barcos[barco_en_canal].encallado == False:
            if len(canal.barcos_encallados)>0:
                for barco_encallado in canal.barcos_encallados:
                    if barcos[barco_en_canal].ubicacion < barcos[barco_encallado].ubicacion:
                        if (barcos[barco_en_canal].ubicacion + barcos[barco_en_canal].velocidad) >= barcos[barco_encallado].ubicacion:
                            print(f"El barco {barco_en_canal} no puede avanzar ya que el {barco_encallado} se encuentra encallado mas adelante")
                            x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                            canal.dinero -= x
                            canal.dinero_gastado += x
                            canal.dinero_gastado_hora += x
                            print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")
                        else:
                            if barcos[barco_en_canal].tipo == "Buque" and barcos[barco_en_canal].tiempo_averia < parametros.TIEMPO_AVERIA_BUQUE:
                                print(f"El barco {barco_en_canal} se encuentra averiado y esta en proceso de reparación")
                                barcos[barco_en_canal].tiempo_averia += 1
                                x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                                canal.dinero -= x
                                canal.dinero_gastado += x
                                canal.dinero_gastado_hora += x
                                print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")
                            else:
                                barcos[barco_en_canal].desplazarse()
                                if barcos[barco_en_canal].ubicacion > canal.largo:
                                    if barcos[barco_en_canal].tipo == "Carguero" and barcos[barco_en_canal].evento_especial == True:
                                        canal.barcos.remove(barco_en_canal)
                                        canal.barcos_pasaron += 1
                                        barcos[barco_en_canal].ubicacion = 0
                                        print(f"El barco {barco_en_canal} ha llegado al final del canal, pero no tiene dinero para pagar porque fue atacado por piratas")
                                    else:
                                        canal.barcos.remove(barco_en_canal)
                                        canal.barcos_pasaron += 1
                                        barcos[barco_en_canal].ubicacion = 0
                                        canal.dinero_recibido += canal.cobro_uso
                                        canal.dinero_recibido_hora += canal.cobro_uso
                                        canal.dinero += canal.cobro_uso
                                        print(f"El barco {barco_en_canal} ha llegado al final del canal")
                                
                                else:
                                    if barcos[barco_en_canal].encallar() == True and barcos[barco_en_canal].nombre not in canal.barcos_encallados:
                                        canal.barcos_encallados.append(barcos[barco_en_canal].nombre)
                                        canal.barcos_encallaron += 1
                                        print(f"El barco {barcos[barco_en_canal].nombre} ha encallado en el KM {barcos[barco_en_canal].ubicacion}")
                                    elif barcos[barco_en_canal].evento_especial == False: 
                                        barcos[barco_en_canal].ejecutar_evento_especial(canal)
                                    barcos[barco_en_canal].tiempo_averia += 1  
                                    x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                                    canal.dinero -= x
                                    canal.dinero_gastado += x
                                    canal.dinero_gastado_hora += x
                                    print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")
                    else:
                        if barcos[barco_en_canal].tipo == "Buque" and barcos[barco_en_canal].tiempo_averia < parametros.TIEMPO_AVERIA_BUQUE:
                            print(f"El barco {barco_en_canal} se encuentra averiado y esta en proceso de reparación")
                            barcos[barco_en_canal].tiempo_averia += 1
                            x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                            canal.dinero -= x
                            canal.dinero_gastado += x
                            canal.dinero_gastado_hora += x
                            print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")
                        else:
                            barcos[barco_en_canal].desplazarse()
                            if barcos[barco_en_canal].ubicacion > canal.largo:
                                if barcos[barco_en_canal].tipo == "Carguero" and barcos[barco_en_canal].evento_especial == True:
                                    canal.barcos.remove(barco_en_canal)
                                    canal.barcos_pasaron += 1
                                    barcos[barco_en_canal].ubicacion = 0
                                    print(f"El barco {barco_en_canal} ha llegado al final del canal, pero no tiene dinero para pagar porque fue atacado por piratas")
                                else:
                                    canal.barcos.remove(barco_en_canal)
                                    canal.barcos_pasaron += 1
                                    barcos[barco_en_canal].ubicacion = 0
                                    canal.dinero_recibido += canal.cobro_uso
                                    canal.dinero_recibido_hora += canal.cobro_uso
                                    canal.dinero += canal.cobro_uso
                                    print(f"El barco {barco_en_canal} ha llegado al final del canal")
                            else:
                                if barcos[barco_en_canal].encallar() == True and barcos[barco_en_canal].nombre not in canal.barcos_encallados:
                                    canal.barcos_encallados.append(barcos[barco_en_canal].nombre)
                                    canal.barcos_encallaron += 1
                                    print(f"El barco {barcos[barco_en_canal].nombre} ha encallado en el KM {round(barcos[barco_en_canal].ubicacion,1)}")
                                elif barcos[barco_en_canal].evento_especial == False: 
                                    barcos[barco_en_canal].ejecutar_evento_especial(canal)
                                barcos[barco_en_canal].tiempo_averia += 1  
                                x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                                canal.dinero -= x
                                canal.dinero_gastado += x
                                canal.dinero_gastado_hora += x
                                print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")

            else:     
                if barcos[barco_en_canal].tipo == "Buque" and barcos[barco_en_canal].evento_especial == True and barcos[barco_en_canal].tiempo_averia < parametros.TIEMPO_AVERIA_BUQUE:
                            print(f"El barco {barco_en_canal} se encuentra averiado y esta en proceso de reparación")
                            barcos[barco_en_canal].tiempo_averia += 1
                            x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                            canal.dinero -= x
                            canal.dinero_gastado += x
                            canal.dinero_gastado_hora += x
                            print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")
                else:
    
                    barcos[barco_en_canal].desplazarse()
                    if barcos[barco_en_canal].ubicacion > canal.largo:
                        if barcos[barco_en_canal].tipo == "Carguero" and barcos[barco_en_canal].evento_especial == True:
                            canal.barcos.remove(barco_en_canal)
                            canal.barcos_pasaron += 1
                            barcos[barco_en_canal].ubicacion = 0
                            print(f"El barco {barco_en_canal} ha llegado al final del canal, pero no tiene dinero para pagar porque fue atacado por piratas")
                        else:
                            canal.barcos.remove(barco_en_canal)
                            canal.barcos_pasaron += 1
                            barcos[barco_en_canal].ubicacion = 0
                            canal.dinero_recibido += canal.cobro_uso
                            canal.dinero_recibido_hora += canal.cobro_uso
                            canal.dinero += canal.cobro_uso
                            print(f"El barco {barco_en_canal} ha llegado al final del canal")
                    else:
                        if barcos[barco_en_canal].encallar() == True:
                            canal.barcos_encallados.append(barcos[barco_en_canal].nombre)
                            canal.barcos_encallaron += 1
                            print(f"El barco {barcos[barco_en_canal].nombre} ha encallado en el KM {round(barcos[barco_en_canal].ubicacion,1)}")
                        elif barcos[barco_en_canal].evento_especial == False: 
                            barcos[barco_en_canal].ejecutar_evento_especial(canal)    
                        barcos[barco_en_canal].tiempo_en_canal += 1
                        barcos[barco_en_canal].tiempo_averia +=1
                        x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
                        canal.dinero -= x
                        canal.dinero_gastado += x
                        canal.dinero_gastado_hora += x
                        print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")
                        

        else:
            x = round(c.convert(barcos[barco_en_canal].costo_mantención, barcos[barco_en_canal].moneda_origen, "USD"),1)
            canal.dinero -= x
            canal.dinero_gastado += x
            canal.dinero_gastado_hora += x
            print(f"El canal le paga {x} al barco {barco_en_canal} por costos de mantencíon")

        for tripulante in barcos[barco_en_canal].tripulacion:
            if tripulantes[tripulante].tipo == "DCCarguero" and tripulantes[tripulante].evento == False:
                barcos[barco_en_canal].carga_maxima += parametros.CARGA_EXTRA_CARGUERO
                tripulantes[tripulante].evento = True


        for paquete in barcos[barco_en_canal].mercancia:
            for tripulante in barcos[barco_en_canal].tripulacion:
                if mercancias[paquete].tipo == "alimentos" and tripulantes[tripulante].tipo =="DCCocinero" and tripulantes[tripulante].cocinar == False:
                    mercancias[paquete].tiempo_exp = mercancias[paquete].tiempo_exp * 2
                    tripulantes[tripulante].cocinar = True
            if barcos[barco_en_canal].tiempo_en_canal > mercancias[paquete].tiempo_exp and mercancias[paquete].expiro == False:
                mercancias[paquete].expirar(canal, barcos[barco_en_canal])

        
                        
        




    if canal.dinero <= 0:
        print("Se acabaron los fondos del canal, perdiste :(")
        quit()

    print()
    for barco in canal.barcos:
        print(f"El barco {barcos[barco].nombre} se encuentra en el KM {round(barcos[barco].ubicacion,1)}")
    print()
    print(f"Dinero recaudado: {round(canal.dinero_recibido_hora,1)}")
    print(f"Dinero gastado: {round(canal.dinero_gastado_hora,1)}")
    print()


    canal.horas_simuladas += 1




    pass
def mostrar_estado(canal):
    print()
    print("ESTADO DEL CANAL")
    print()
    print("--------------------------------------")
    print()
    print(f"{canal.nombre} de {canal.largo} KM de largo, con dificultad {canal.dificultad}.")
    print(f"Horas simuladas: {canal.horas_simuladas}")
    print(f"Dinero disponible: {round(canal.dinero,1)}")
    print(f"Dinero gastado: {round(canal.dinero_gastado,1)}")
    print(f"Dinero recibido: {round(canal.dinero_recibido,1)}")
    print(f"Numero de barcos que pasaron: {canal.barcos_pasaron}")
    print(f"Numero de barcos que encallaron: {canal.barcos_encallaron}")
    print(f"Eventos especiales ocurridos: {canal.eventos_ocurridos}")
    print()
    pass            