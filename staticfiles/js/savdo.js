class BasePokritiya{
    constructor(
        full=false,
        id=NaN,//done
        nazvaniye_system=NaN,
        base_artikul=NaN, 
        dlina=NaN,
        tip_pokritiya=NaN,//done
        splav=NaN,
        tip_zak=NaN,
        combination=NaN,
        brend_kraska_sn=NaN,
        kod_kraska_sn=NaN,
        brend_kraska_vn=NaN,
        kod_kraska_vn=NaN,
        kod_dekor_sn=NaN,
        svet_dekplonka_snaruji=NaN,
        kod_dekor_vn=NaN,
        svet_dekplonka_vnutri=NaN,
        kod_lam_sn=NaN,
        svet_lamplonka_snaruji=NaN,
        kod_lam_vn=NaN,
        svet_lamplonka_vnutri=NaN,
        kod_anod_sn=NaN,
        kod_anod_vn=NaN,
        contactnost_anod=NaN,
        tip_anod=NaN,
        sposob_anod=NaN,
        kod_nakleyki=NaN,
        nadpis_nakleyki=NaN,
        baza_profiley=NaN,
        gruppa_materialov=NaN,
        kratkiy_tekst=NaN,
        sap_code=NaN,
        krat=NaN,
        comment=NaN,
        dilina_pressa =NaN,
        zavod=NaN,

        online_id=NaN,
        nazvaniye_ruchnoy=NaN,
        svet_product=NaN,//done
        group_zakup=NaN,
        group=NaN,
        tip=NaN,//done
        segment=NaN,
        buxgalter_tovar=NaN,
        buxgalter_uchot=NaN,//done
        bazoviy_edin=NaN,//done
        alter_edin=NaN,//done
        stoimost_baza=NaN,//done
        stoimost_alter=NaN,
        status_online=NaN,
        zavod_name=NaN,
        diller=NaN,
        tip_clienta=NaN, 
        is_termo=false,
        is_active=false,
        status_name =NaN
        ) {
            this.full=full;
            this.id=id;//done
            this.nazvaniye_system=nazvaniye_system;//done
            this.base_artikul=base_artikul;//done
            this.dlina=dlina;//done
            this.tip_pokritiya=tip_pokritiya;//done
            this.splav=splav;//done
            this.tip_zak=tip_zak;//done
            this.combination=combination;//done
            this.brend_kraska_sn=brend_kraska_sn;//done
            this.kod_kraska_sn=kod_kraska_sn;//done
            this.brend_kraska_vn=brend_kraska_vn;//done
            this.kod_kraska_vn=kod_kraska_vn;//done
            this.kod_dekor_sn=kod_dekor_sn;//done
            this.svet_dekplonka_snaruji=svet_dekplonka_snaruji;//done
            this.kod_dekor_vn=kod_dekor_vn;//done
            this.svet_dekplonka_vnutri=svet_dekplonka_vnutri;//done
            this.kod_lam_sn=kod_lam_sn;//done
            this.svet_lamplonka_snaruji=svet_lamplonka_snaruji;//done
            this.kod_lam_vn=kod_lam_vn;//done
            this.svet_lamplonka_vnutri=svet_lamplonka_vnutri;//done
            this.kod_anod_sn=kod_anod_sn;//done
            this.kod_anod_vn=kod_anod_vn;//done
            this.contactnost_anod=contactnost_anod;//done
            this.tip_anod=tip_anod;//done
            this.sposob_anod=sposob_anod;//done
            this.kod_nakleyki=kod_nakleyki;//done
            this.nadpis_nakleyki=nadpis_nakleyki;
            this.baza_profiley=baza_profiley;
            this.gruppa_materialov=gruppa_materialov;
            this.kratkiy_tekst=kratkiy_tekst;//done
            this.sap_code=sap_code;//done
            this.krat=krat;//done
            this.comment=comment;
            this.dilina_pressa =dilina_pressa;
            this.zavod=zavod;//done
            this.online_id=online_id;//done
            this.nazvaniye_ruchnoy=nazvaniye_ruchnoy;//done
            this.svet_product=svet_product;//done
            this.group_zakup=group_zakup;//done
            this.group=group;//done
            this.tip=tip;//done
            this.segment=segment;//done
            this.buxgalter_tovar=buxgalter_tovar;//done
            this.buxgalter_uchot=buxgalter_uchot;//done
            this.bazoviy_edin=bazoviy_edin;//done
            this.alter_edin=alter_edin;//done
            this.stoimost_baza=stoimost_baza;//done
            this.stoimost_alter=stoimost_alter;//done
            this.status_online=status_online;//done
            this.zavod_name=zavod_name;//done
            this.diller=diller;
            this.tip_clienta=tip_clienta;
            this.is_termo=is_termo;//done
            this.is_active=is_active;//done
            this.status_name=status_name;//done
    }
    get_kratkiy_tekst(){
        this.group='NAAAAN'
        switch(this.id){
            case 1:  if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_nakleyki){
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                        }
                    }else{
                        if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
                        }
    
                    }
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
            
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
            
                            }
                        }else{
                            if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
            
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_kraska_sn +'/'+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
            
                            }
        
                        }
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                } break;
            case 2:  if(!this.is_termo){

                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
    
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
        
                        }
    
                    }else{
    
                        if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
        
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
        
                        }
                    }
    
                    
    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
        
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
        
        
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
            
                            }
        
                        }else{
        
                            if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
            
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
            
                            }
                        }  
        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 3:  if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_nakleyki){
    
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
        
                        }
    
                    }else{
    
                        if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
        
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +' ' +this.kod_nakleyki,'accept':false}
        
                        }
                    }
    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_nakleyki){
        
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
            
                            }
        
                        }else{
        
                            if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod  && this.segment){
            
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn+'/'+this.brend_kraska_vn+this.kod_kraska_vn+' ' +this.kod_nakleyki,'accept':false}
            
                            }
                        }
        
        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                } break;
            case 4: if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki){
    
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
    
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                        }
    
                    }else{
    
                        if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod  && this.segment){
        
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
                        }
                    } 
    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_lam_vn && this.kod_lam_sn && this.kod_nakleyki){
        
        
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy  && this.segment){
        
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
            
                            }
        
                        }else{
        
                            if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod  && this.segment){
            
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn + this.kod_kraska_vn +'_'+this.kod_lam_sn+'/'+this.kod_lam_vn + ' ' +this.kod_nakleyki,'accept':false}
            
                            }
                        } 
        
        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                }break;
            case 5:  if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.kod_kraska_sn && this.kod_dekor_sn && this.kod_nakleyki){
    
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
    
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':false}
        
                        }
    
                    }else{
    
                        if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
        
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'_'+this.kod_dekor_sn + ' ' +this.kod_nakleyki,'accept':false}
        
                        }
                    }
    
    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.brend_kraska_sn && this.brend_kraska_vn && this.kod_kraska_sn && this.kod_kraska_vn && this.kod_dekor_sn && this.kod_dekor_vn  && this.kod_nakleyki){
        
        
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
        
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':false}
            
                            }
        
                        }else{
        
                            if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
            
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.brend_kraska_sn+ this.kod_kraska_sn +'/'+this.brend_kraska_vn+this.kod_kraska_vn+'_'+this.kod_dekor_sn+'/'+this.kod_dekor_vn + ' ' +this.kod_nakleyki,'accept':false}
            
                            }
                        }
        
        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
                } break;
            case 6:  if(!this.is_termo){
                if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_nakleyki && this.contactnost_anod){
    
                    if(this.is_active){
                        if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                        }
    
                    }else{
    
                        if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                        }else{
                            return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn + ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                        }
                    }
    
                }else{
                    return {'text':'XXXXXXXX','accept':false}
                }
                }else{
                    if(this.splav && this.tip_zak && this.dlina && this.kod_anod_sn && this.kod_anod_vn && this.kod_nakleyki && this.contactnost_anod){
        
                        if(this.is_active){
                            if (this.online_id && this.nazvaniye_ruchnoy && this.segment){
        
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                            }
        
                        }else{
        
                            if (this.nazvaniye_ruchnoy && this.svet_product && this.group_zakup && this.group && this.tip && this.bazoviy_edin && this.status_online && this.zavod && this.segment){
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':true}
                            }else{
                                return {'text':this.splav + this.tip_zak + ' L' + this.dlina +' ' + this.kod_anod_sn +'/'+this.kod_anod_vn+ ' ' + this.contactnost_anod + ' ' + this.kod_nakleyki,'accept':false}
                            }
                        }
        
        
        
                    }else{
                        return {'text':'XXXXXXXX','accept':false}
                    }
        
                } break;
        }
        
    }
  }

var nakleyka_list = document.getElementById('nakleyka_list').outerHTML

function front_piece(start=1,end=6){
    text =""
    for (let i = start; i < end; i++) {
        nakleyki = nakleyka_list.replace('nakleyka_list',"nakleyka"+String(i))
    
        nakleyki = nakleyki.replace('onchange=""','onchange="create_kratkiy_tekst('+String(i)+')"')
    
        text +=`
        <tr id='table_tr` +String(i)+`' >
                                    
        <td >
            <div class="input-group input-group-sm mb-1">
   
                <div class="dropdown">
                    <button class="btn btn-primary dropdown-toggle btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    <span id='icon_btn`+String(i)+`'><i class="bi bi-three-dots-vertical"></i></span>
                    </button>
                    <ul class="dropdown-menu">
                        <li style='cursor:pointer;font-size:14px'id='create_btn`+String(i)+`' data-bs-toggle='popover' title='Yangi sozdaniya qilish uchun ishlatiladi' data-bs-content='this is bots content'><a class="dropdown-item" onclick="create(`+String(i)+`)" >     <i class="bi bi-plus-circle mr-2"></i>Создание</a></li>
                        <li style='cursor:pointer;font-size:14px'id='activate_btn`+String(i)+`'><a class="dropdown-item" onclick="activate(`+String(i)+`)" > <i class="bi bi-award-fill mr-2"></i>Активация</a></li>
                        <li style='cursor:pointer;font-size:14px'><a class="dropdown-item" onclick="copy_tr(`+String(i)+`)"   ><i class="bi bi-clipboard mr-2"></i>Дублировать</a></li>
                        <li style='cursor:pointer;font-size:14px'><a class="dropdown-item" onclick="artukil_clear(`+String(i)+`)"  id='clear_btn`+String(i)+`' ><i class="bi bi-x-circle mr-2"></i>Очистить</a></li>
                    </ul>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div><span class ='nazvaniye_system` +String(i)+`'style="text-transform: uppercase;" style="font-size: 12px;"></span></div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class=" form-control basic_artikul" style="background-color:#ddebf7; width: 140px; font-size:10px " disabled id="artikul`+String(i)+`" ></select>
                <span style='display:none' id ='nakleyka_codd` +String(i)+`'></span>
            </div>
        </td>
        
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <input type="text" class="form-control " style='width:50px' onkeyup='create_kratkiy_tekst(`+String(i)+`)' disabled aria-describedby="inputGroup-sizing-sm" name ='length`+String(i)+`' id="length`+String(i)+`" maxlength="4" >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 165px;text-transform: uppercase; font-size:12px; padding-right:0px;" onchange="tip_pokritiya_selected(`+String(i)+`,this.value)" disabled id='tip_pokritiya`+String(i)+`' required>
                    <option  selected></option>
                    <option value="1" >Неокрашенный</option>
                    <option value="2">Белый</option>
                    <option value="3">Окрашенный</option>
                    <option value="4">Ламинированный</option>
                    <option value="5">Сублимированный</option>
                    <option value="6">Анодированный</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
        
            <select class="form-select" aria-label="" style="width: 50px;"  disabled id='splav`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected ></option>
                <option value="63" >63</option>
            </select>
            
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  style="width: 60px;">
            <select class="form-select" aria-label="" style="width: 50px;!important"  disabled id='tip_zakalyonnosti`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value="" selected></option>
                <option value="T4" >T4</option>
                <option value="T6" >T6</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" style="font-size: small; text-transform: uppercase; width:130px">
                <div>
                    <span class =' text-center pl-1' style="font-size: small; text-transform: uppercase;" id ='combination` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" >
           <select class="form-select form-select-sm text-center"  style="width:65px;border-color:#fc2003;display:none" id='brand_k_snaruji`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                <option  value="0" selected></option>
                <option value="NT1">NT1</option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;">
            <select class="form-select form-select-sm text-center"  style="width:100px;border-color:#fc2003;display:none" id='code_kraski_snar`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                                    <option  value="0" selected></option>
                                    <option value="MF">MF</option>
                                    <option value="8M01">8M01</option>
                                    <option value="6029">6029</option>
                                    <option value="1013">1013</option>
                                    <option value="7M43">7M43</option>
                                    <option value="8002">8002</option>
                                    <option value="7M24">7M24</option>
                                    <option value="7M16">7M16</option>
                                    <option value="7043">7043</option>
                                    <option value="7021">7021</option>
                                    <option value="7015">7015</option>
                                    <option value="7039">7039</option>
                                    <option value="7011">7011</option>
                                    <option value="7M47">7M47</option>
                                    <option value="9016">9016</option>
                                    <option value="7016">7016</option>
                                    <option value="2654">2654</option>
                                    <option value="9010">9010</option>
                                    <option value="9M05">9M05</option>
                                    <option value="9005">9005</option>
                                    <option value="3884">3884</option>
                                    <option value="3774">3774</option>
                                    <option value="235G">235G</option>
                                    <option value="7M21">7M21</option>
                                    <option value="355F">355F</option>
                                    <option value="8001">8001</option>
                                    <option value="8019">8019</option>
                                    <option value="8017">8017</option>
                                    <option value="9006">9006</option>
                                    <option value="306G">306G</option>
                                    <option value="9011">9011</option>
                                    <option value="2M06">2M06</option>
                                    <option value="8M19">8M19</option>
                                    <option value="8003">8003</option>
                                    <option value="2900">2900</option>
                                    <option value="7037">7037</option>
                                    <option value="281F">281F</option>
                                    <option value="1019">1019</option>
                                    <option value="7M22">7M22</option>
                                    <option value="7M31">7M31</option>
                                    <option value="9M07">9M07</option>
                                    <option value="9M16">9M16</option>
                                    <option value="7M35">7M35</option>
                                    <option value="9007">9007</option>
                                    <option value="5002">5002</option>
                                    <option value="7024">7024</option>
                                    <option value="2604">2604</option>
                                    <option value="7035">7035</option>
                                    <option value="7M36">7M36</option>
                                    <option value="7042">7042</option>
                                    <option value="9M03">9M03</option>
                                    <option value="7006">7006</option>
                                    <option value="9M04">9M04</option>
                                    <option value="9003">9003</option>
                                    <option value="2M04">2M04</option>
                                    <option value="283F">283F</option>
                                    <option value="7038">7038</option>
                                    <option value="1035">1035</option>
                                    <option value="7M39">7M39</option>
                                    <option value="2303">2303</option>
                                    <option value="3020">3020</option>
                                    <option value="8M24">8M24</option>
                                    <option value="7M12">7M12</option>
                                    <option value="9001">9001</option>
                                    <option value="7M06">7M06</option>
                                    <option value="8000">8000</option>
                                    <option value="1015">1015</option>
                                    <option value="7030">7030</option>
                                    <option value="8024">8024</option>
                                    <option value="1376">1376</option>
                                    <option value="S352">S352</option>
                                    <option value="8077">8077</option>
                                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select form-select-sm text-center"  style="width:65px;border-color:#fc2003;display:none" id='brand_k_vnutri`+String(i)+`' onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                <option  value="0" selected></option>
                <option value="A">A</option>
                <option value="B">B</option>
                <option value="R">R</option>
                <option value="T">T</option>
                <option value="J">J</option>
                <option value="P">P</option>
                <option value="M">M</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 100px;">
            <select class="form-select form-select-sm text-center"  style="width:100px;border-color:#fc2003;display:none" id='code_kraski_vnut`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)" required>
                                    <option  value="0" selected></option>
                                    <option value="MF">MF</option>
                                    <option value="8M01">8M01</option>
                                    <option value="6029">6029</option>
                                    <option value="1013">1013</option>
                                    <option value="7M43">7M43</option>
                                    <option value="8002">8002</option>
                                    <option value="7M24">7M24</option>
                                    <option value="7M16">7M16</option>
                                    <option value="7043">7043</option>
                                    <option value="7021">7021</option>
                                    <option value="7015">7015</option>
                                    <option value="7039">7039</option>
                                    <option value="7011">7011</option>
                                    <option value="7M47">7M47</option>
                                    <option value="9016">9016</option>
                                    <option value="7016">7016</option>
                                    <option value="2654">2654</option>
                                    <option value="9010">9010</option>
                                    <option value="9M05">9M05</option>
                                    <option value="9005">9005</option>
                                    <option value="3884">3884</option>
                                    <option value="3774">3774</option>
                                    <option value="235G">235G</option>
                                    <option value="7M21">7M21</option>
                                    <option value="355F">355F</option>
                                    <option value="8001">8001</option>
                                    <option value="8019">8019</option>
                                    <option value="8017">8017</option>
                                    <option value="9006">9006</option>
                                    <option value="306G">306G</option>
                                    <option value="9011">9011</option>
                                    <option value="2M06">2M06</option>
                                    <option value="8M19">8M19</option>
                                    <option value="8003">8003</option>
                                    <option value="2900">2900</option>
                                    <option value="7037">7037</option>
                                    <option value="281F">281F</option>
                                    <option value="1019">1019</option>
                                    <option value="7M22">7M22</option>
                                    <option value="7M31">7M31</option>
                                    <option value="9M07">9M07</option>
                                    <option value="9M16">9M16</option>
                                    <option value="7M35">7M35</option>
                                    <option value="9007">9007</option>
                                    <option value="5002">5002</option>
                                    <option value="7024">7024</option>
                                    <option value="2604">2604</option>
                                    <option value="7035">7035</option>
                                    <option value="7M36">7M36</option>
                                    <option value="7042">7042</option>
                                    <option value="9M03">9M03</option>
                                    <option value="7006">7006</option>
                                    <option value="9M04">9M04</option>
                                    <option value="9003">9003</option>
                                    <option value="2M04">2M04</option>
                                    <option value="283F">283F</option>
                                    <option value="7038">7038</option>
                                    <option value="1035">1035</option>
                                    <option value="7M39">7M39</option>
                                    <option value="2303">2303</option>
                                    <option value="3020">3020</option>
                                    <option value="8M24">8M24</option>
                                    <option value="7M12">7M12</option>
                                    <option value="9001">9001</option>
                                    <option value="7M06">7M06</option>
                                    <option value="8000">8000</option>
                                    <option value="1015">1015</option>
                                    <option value="7030">7030</option>
                                    <option value="8024">8024</option>
                                    <option value="1376">1376</option>
                                    <option value="S352">S352</option>
                                    <option value="8077">8077</option>
                                </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 75px;" onchange="svet_dekplonka_snaruji_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_snaruji`+String(i)+`' disabled>
                <option  value="" selected></option>
                <option value="Золотой Дуб 7777" >7777</option>
                <option value="Махагон 3701">3701</option>
                <option value="3D 3702">3702</option>
                <option value="Дуб мокко">8888</option>
                <option value="Шеф. сер. дуб">9999</option>
                <option value="XXXX">XXXX</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_snaruji` +String(i)+`' disabled ></span></em>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1"  >    
            <select class="form-select" aria-label="" style="width: 75px;" onchange="svet_dekplonka_vnutri_selected(`+String(i)+`,this.value)"  id='svet_dekplonka_vnutri`+String(i)+`' disabled>
                <option  value="" selected></option>
                <option value="Золотой Дуб 7777" >7777</option>
                <option value="Махагон 3701">3701</option>
                <option value="3D 3702">3702</option>
                <option value="Дуб мокко">8888</option>
                <option value="Шеф. сер. дуб">9999</option>
                <option value="XXXX">XXXX</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                <em><span class =' text-center ' style="font-size: 10px;  font-weight: bold; text-transform: uppercase;" id ='code_dekplonka_vnutri` +String(i)+`' disabled></span></em>
                </div>
            </div>
        </td>

        

        <td >
            <div class="input-group input-group-sm mb-1">    
            <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_snaruji_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_snaruji`+String(i)+`'>
                <option  value="" selected></option>
                <option value="2036" >Золотой дуб</option>
                <option value="2048">Дуб мокко</option>
                <option value="2007">Красный орех</option>
                <option value="2012">Орех</option>
                <option value="3086">Шеффелдский дуб серый</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="3001">Терновый дуб</option>
                <option value="3002">Шеф Альпийский дуб</option>
                <option value="3003">Гранитовый шеф дуб</option>
                <option value="3042">Дерево бальза</option>
                <option value="3062">Грецкий орех</option>
                <option value="3043">Вишня амаретто</option>
                <option value="3059">Орех терра</option>
                <option value="3058">Грецкий орех амаретто</option>
                <option value="3077">Винчестер</option>
                <option value="3081">Шеффелдский дуб светлый</option>
                <option value="3094">Орех Ребраун</option>
                <option value="1004">Метбраш платин</option>
                <option value="1005">Метбраш серый кварц</option>
                <option value="1006">Метбраш серый антрацит</option>
                <option value="XXXX">XXXX</option>
            </select>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%;" id ='code_lamplonka_snaruji` +String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <select class="form-select" aria-label="" style="width: 220px;" onchange="svet_lamplonka_vnutri_selected(`+String(i)+`,this.value)" disabled id='svet_lamplonka_vnutri`+String(i)+`'>
                    <option  value="" selected></option>
                    <option value="2036" >Золотой дуб</option>
                <option value="2048">Дуб мокко</option>
                <option value="2007">Красный орех</option>
                <option value="2012">Орех</option>
                <option value="3086">Шеффелдский дуб серый</option>
                <option value="1012">Алюкс антрацит</option>
                <option value="3001">Терновый дуб</option>
                <option value="3002">Шеф Альпийский дуб</option>
                <option value="3003">Гранитовый шеф дуб</option>
                <option value="3042">Дерево бальза</option>
                <option value="3062">Грецкий орех</option>
                <option value="3043">Вишня амаретто</option>
                <option value="3059">Орех терра</option>
                <option value="3058">Грецкий орех амаретто</option>
                <option value="3077">Винчестер</option>
                <option value="3081">Шеффелдский дуб светлый</option>
                <option value="3094">Орех Ребраун</option>
                <option value="1004">Метбраш платин</option>
                <option value="1005">Метбраш серый кварц</option>
                <option value="1006">Метбраш серый антрацит</option>
                <option value="XXXX">XXXX</option>
                </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <div>
                    <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;padding-left:35%" id='code_lamplonka_vnutri`+String(i)+`'></span>
                </div>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" >
            <div id='anod`+String(i)+`' class='anood'  style="width: 75px;border-color:red; display:none;" >
                <select class="form-select kod_anod_snar" aria-label="" style=" width: 100px; border-color:#fc2003;!important; display:none" onchange="code_svet_anodirovki_snaruji_selected(`+String(i)+`,this.value)"  id='code_svet_anodirovki_snaruji`+String(i)+`' required></select>         
            </div>          
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <div id='anod_vnutr`+String(i)+`'  style="width: 75px;display:none;border-color:red;">
                <select class="form-select kod_anod_vnutri" aria-label="" style="width: 75px;border-color:#fc2003;margin-right:15px;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='code_svet_anodirovki_vnutr`+String(i)+`' required></select>       
            </div>
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1" style="width: 60px;">
            <select class="form-select" aria-label=""   disabled id='contactnost_anodirovki`+String(i)+`'  onchange="create_kratkiy_tekst(`+String(i)+`)">
                <option  value=""></option>
                <option value="YC" >YC</option>
                <option value="NC">NC</option>
            </select>
            </div>
        </td>
        <td style='display:none'>
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; font-weight: bold; text-transform: uppercase;" id='tip_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td style='display:none' >
            <div class="input-group input-group-sm mb-1">
            <div>
                <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='sposob_anodirovki`+String(i)+`'></span>
            </div>
            </div>
        </td>
        <td >`
        text +=nakleyki

        text += `
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
                <span  style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='nadpis_nakleyki`+String(i)+`'></span>
            </div>
        </td>
        <td >
        <span  style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='baza_profiley`+String(i)+`'></span>
        </td>
        
        <td >
            <span  style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='gruppa_materialov`+String(i)+`'>ALUGP</span>   
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:250px; font-weight: bold; text-transform: uppercase;" id='kratkiy_tekst`+String(i)+`'></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
        
            <input type='text' class=" form-control " style=" width: 150px; font-size:10px;" id='sap_code_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
        
            </div>
        </td> 
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style=" width: 250px; font-size:10px;"  id='kratkiy_tekst_ruchnoy`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        
        <td >
            <div class="input-group input-group-sm mb-1">
                <textarea   rows='1' class=" form-control " style="width: 220px; font-size:10px;height:32px" id='comment`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type="text" class="form-control "  style='width:90px;'   aria-describedby="inputGroup-sizing-sm" onkeyup='create_kratkiy_tekst(`+String(i)+`)' id="dilina_pressa`+String(i)+`"  >    
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 90px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;border-color:red;" onchange="create_kratkiy_tekst(`+String(i)+`)"  id='zavod`+String(i)+`' required>
                <option  selected></option>
                <option value="ZAVOD ALUMIN NAVOIY" >Benkam</option>
                <option value="ZAVOD ALUMIN">Jomiy</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="border-color:red; width: 75px; font-size:10px; display:none;" id='online_savdo_id`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <textarea   rows='1' class=" form-control " style="border-color:red; width: 220px; font-size:10px; display:none; " id='nazvaniye_ruchnoy`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></textarea >
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 110px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='svet_product`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option   value="LAM">LAM</option>
            <option   value="Anod">Anod</option>
            <option   value="COLOUR">COLOUR</option>
            <option   value="VAKUM &amp; 3D">VAKUM &amp; 3D</option>
            <option   value="WHITE">WHITE</option>
            <option   value="Без цвета">Без цвета</option>
        </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 230px;text-transform: uppercase; font-size:12px; padding-right:0px;  border-color:red;display:none;" id='group_zakup`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
            <option  selected></option>
            <option value="Kabina">Kabina</option>
            <option value="Alumin WHITE (B.N)">Alumin WHITE (B.N)</option>
            <option value="Aksessuar Import (SAP)">Aksessuar Import (SAP)</option>
            <option value="Alumin VAKUM (B.N)">Alumin VAKUM (B.N)</option>
            <option value="Metal">Metal</option>
            <option value="Aksessuar UZ Tapoich">Aksessuar UZ Tapoich</option>
            <option value="Alumin COLOUR (Navoiy)">Alumin COLOUR (Navoiy)</option>
            <option value="Alumin VAKUM (Navoiy)">Alumin VAKUM (Navoiy)</option>
            <option value="Alumin WHITE (Navoiy)">Alumin WHITE (Navoiy)</option>
            <option value="Alumin Anod (Navoiy)">Alumin Anod (Navoiy)</option>
            <option value="PVX OQ (Navoiy)">PVX OQ (Navoiy)</option>
            <option value="Butilchita">Butilchita</option>
            <option value="Aksessuar Rezina">Aksessuar Rezina</option>
            <option value="Radiator">Radiator</option>
            <option value="Aksessuar UZ">Aksessuar UZ</option>
            <option value="Alucobond">Alucobond</option>
            <option value="VITYAJNOYE USTROYSTVA">VITYAJNOYE USTROYSTVA</option>
            <option value="Aksessuar Import">Aksessuar Import</option>
            <option value="Radiator (IMPORT)">Radiator (IMPORT)</option>
            <option value="Radiator SAP (IMPORT)">Radiator SAP (IMPORT)</option>
            <option value="PVX LAM (Navoiy)">PVX LAM (Navoiy)</option>
            <option value="Rezina Tpv">Rezina Tpv</option>
            <option value="Granula">Granula</option>
            <option value="Granit">Granit</option>
            <option value="Setka">Setka</option>
            <option value="Kraska">Kraska</option>
            <option value="Gazoblok">Gazoblok</option>
            <option value="Paket">Paket</option>
            <option value="Alumin Lam">Alumin Lam</option>
            <option value="Alumin COLOUR">Alumin COLOUR</option>
            <option value="Alumin VAKUM">Alumin VAKUM</option>
            <option value="Alumin WHITE">Alumin WHITE</option>
            <option value="Radiator (Panel) AKFA (UZ)">Radiator (Panel) AKFA (UZ)</option>
            <option value="Radiator (Panel) ROYAL (UZ)">Radiator (Panel) ROYAL (UZ)</option>
            <option value="Radiator (Panel) Lider Line (UZ)" >Radiator (Panel) Lider Line (UZ)"</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1" id='group`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'>
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='tipr`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Сырье">Сырье</option>
                <option value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;"  id='tip`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)'required>
                <option  selected></option>
                <option value="Сырье">Сырье</option>
                <option value="Готовый продукт">Готовый продукт</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 145px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='segment`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Нет сегмента">Нет сегмента</option>
                <option value=""></option>
                <option value="Aldoks">Aldoks</option>
                <option value="Стандарт">Стандарт</option>
                <option value="Премиум">Премиум</option>
                <option value="Аксессуар">Аксессуар</option>
                <option value="Falcon">Falcon</option>
                <option value="Mebel">Mebel</option>
                <option value="RETPEN 8-10%">RETPEN 8-10%</option>
                <option value="RETPEN 10-12%">RETPEN 10-12%</option>
                <option value="RETPEN 17%">RETPEN 17%</option>
                <option value="Аксессуар 2">Аксессуар 2</option>
                <option value="Podokonnik EKO">Podokonnik EKO</option>
                <option value="Alumin arzon">Alumin arzon</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 520px;text-transform: uppercase; font-size:12px; padding-right:0px; display:none;" id='buxgalter_tovar`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                    <option  selected></option>
                    <option value="Алюминиевый профиль">Алюминиевый профиль</option>
                    <option value="Неокрашенный алюминиевый профиль">Неокрашенный алюминиевый профиль</option>
                    <option value="Алюминиевый профиль">Алюминиевый профиль</option>
                    <option value="Ламинированный алюминиевый профиль">Ламинированный алюминиевый профиль</option>
                    <option value="Алюминиевый профиль с декоративным покрытием">Алюминиевый профиль с декоративным покрытием</option>
                    <option value="Термоуплотненный окрашенный алюминиевый профиль">Термоуплотненный окрашенный алюминиевый профиль</option>
                    <option value="Неокрашенный алюминиевый профиль">Неокрашенный алюминиевый профиль</option>
                    <option value="Термоуплотненный окрашенный алюминиевый профиль">Термоуплотненный окрашенный алюминиевый профиль</option>
                    <option value="Ламинированный термоуплотненный алюминиевый профиль">Ламинированный термоуплотненный алюминиевый профиль</option>
                    <option value="Алюминиевый профиль (N)">Алюминиевый профиль (N)</option>
                    <option value="Неокрашенный алюминиевый профиль (N)">Неокрашенный алюминиевый профиль (N)</option>
                    <option value="Алюминиевый профиль (N)">Алюминиевый профиль (N)</option>
                    <option value="Ламинированный алюминиевый профиль (N)">Ламинированный алюминиевый профиль (N)</option>
                    <option value="Алюминиевый профиль с декоративным покрытием (N)">Алюминиевый профиль с декоративным покрытием (N)</option>
                    <option value="Термоуплотненный алюминиевый профиль (N)">Термоуплотненный алюминиевый профиль (N)</option>
                    <option value="Неокрашенный алюминиевый профиль (N)">Неокрашенный алюминиевый профиль (N)</option>
                    <option value="Термоуплотненный анодированный алюминиевый профиль (N)">Термоуплотненный анодированный алюминиевый профиль (N)</option>
                    <option value="Термоуплотненный окрашенный алюминиевый профиль (N)">Термоуплотненный окрашенный алюминиевый профиль (N)</option>
                    <option value="Ламинированный термоуплотнённый алюминиевый профиль (N)">Ламинированный термоуплотнённый алюминиевый профиль (N)</option>
                    <option value="Анодированный алюминиевый профиль (N)">Анодированный алюминиевый профиль (N)</option>
                    <option value="Мебельный профиль из алюминия анодированный матовое серебро (N)">Мебельный профиль из алюминия анодированный матовое серебро (N)</option>


            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='buxgalter_uchot`+String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option  value="Штука">Штука</div>
                <option  value="Килограмм">Килограмм</div>
                <option  value="Квадратный метр">Квадратный метр</div>
                <option  value="Метр">Метр</div>
                <option  value="КМП">КМП</div>
                <option  value="Пачка">Пачка</div>
                <option  value="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='bazoviy_edin`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none" id='alter_edin`+ String(i)+`' onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option vlaue="Штука">Штука</div>
                <option vlaue="Килограмм">Килограмм</div>
                <option vlaue="Квадратный метр">Квадратный метр</div>
                <option vlaue="Метр">Метр</div>
                <option vlaue="КМП">КМП</div>
                <option vlaue="Пачка">Пачка</div>
                <option vlaue="Секция">Секция</div>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none;" id='stoimost_baza`+String(i)+`'  onkeyup='create_kratkiy_tekst(`+String(i)+`)'></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <input type='text' class=" form-control " style="width: 75px; font-size:10px; display:none" id='stoimost_alter`+String(i)+`' onkeyup='create_kratkiy_tekst(`+String(i)+`)' ></input>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 155px;text-transform: uppercase; font-size:12px; padding-right:0px; border-color:red;display:none;" id='status`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="Активный">Активный</option>
                <option value="Пассивный">Пассивный</option>
            </select>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <span class =' text-center ' style="font-size: small; width:190px; font-weight: bold; text-transform: uppercase;" id='zavod_name`+String(i)+`'></span>
            </div>
        </td>
        <td >
            <div class="input-group input-group-sm mb-1">
            <select class="form-select" aria-label="" style="width: 75px;text-transform: uppercase; font-size:12px; padding-right:0px;display:none;" id='diller`+String(i)+`'  onchange='create_kratkiy_tekst(`+String(i)+`)' required>
                <option  selected></option>
                <option value="1">Да</option>
                <option value="0">Нет</option>
            </select>
            </div>
        </td>
        <td >
            
        </td>
        </tr>`
    }
    return text
}
text = front_piece()


var table = $('#table-artikul')

table.append(text)



function request_piece(start=1,end=6){
    for (let i = start; i <= end; i++) {
        $('#artikul'+String(i)).select2({
            ajax: {
                url: "/client/imzo-artikul-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.data['Артикул'],system:item.data['Система'],combination:item.data['Комбинация'],code_nakleyka:item.data['Код наклейки'],baza_profiley:item.data['BAZA'],segment:item.data['Сегмент']}
                    })
                };
                }
            }
            });
        
        
        
        var artikulSelect = $('#artikul'+String(i));
        $.ajax({
            type: 'GET',
            url: "/client/imzo-artikul-list"
        }).then(function (data) {
            data.forEach(function(dataItem) {

                var option = new Option(dataItem['Артикул'], data['id'], true, true);
                artikulSelect.append(option).trigger('change');
            
                artikulSelect.trigger({
                    type: 'select2:select',
                    params: {
                        data: dataItem
                    }
                });
            })
        });
        
        
        $("#artikul"+String(i)).on("select2:select", function (e) { 
            var select_val = $(e.currentTarget).val();
            var nazvaniye_system =$('.nazvaniye_system'+String(i));
            var combination = $('#combination'+String(i));
            var tip_pokritiya = $('#tip_pokritiya'+String(i));
            var baza_profiley = $('#baza_profiley'+String(i));
            var segment = $('#segment'+String(i));
            var status = $('#status'+String(i))


            
            // tip_pokritiya.val('').change();
            tip_pokritiya.attr("disabled",false);
            nazvaniye_system.text(e.params.data.system);
            combination.text(e.params.data.combination)
            baza_profiley.text(e.params.data.baza_profiley)
            
            var nakleyka_kode = e.params.data.code_nakleyka
            var segment_text = e.params.data.segment

    
            
            if(status.val()=='Пассивный'){
                segment.val(segment_text)
                if(segment_text == 'Нет сегмента'){
                    segment.css('border-color','red');
                }
            }
            

            
        
        $('.select2-selection__rendered').css('font-size', '15 px');
        
        
        
        var nakleyka = $('#nakleyka'+String(i))
        var nadpis_nakleyki = $('#nadpis_nakleyki'+String(i))
    
        if (nakleyka_kode =='NT1'){
            nakleyka.css('display','block')
            nakleyka.val('NT1')
            nadpis_nakleyki.text('Без наклейки')
        }
        else if( nakleyka_kode !=''){
            var nakleyka_codd = $('#nakleyka_codd'+String(i))
            nakleyka_codd.text(nakleyka_kode)

            if(!data_base[i]){
                console.log('111 com')
                var nakleyka_codd = $('#nakleyka_codd'+String(i))
                nakleyka_codd.text(nakleyka_kode)
                nakleyka.css('display','block')
                nakleyka.val(nakleyka_kode)
                var selectedOption = $('#nakleyka'+String(i)).find('option:selected');
    
                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)
            }else{
                console.log('222 com')
                var pokritiya = data_base[i].id
                if(pokritiya == 1 || pokritiya =='1'){
                    console.log('222 com 222','pokrrr1')
                    nakleyka.css('display','block')
                    nakleyka.val('NT1')
                    nadpis_nakleyki.text('БЕЗ НАКЛЕЙКИ')
                }else{
                    
                    
                    nakleyka.css('display','block')
                    nakleyka.val(nakleyka_kode)
                    var selectedOption = $('#nakleyka'+String(i)).find('option:selected');
        
                    var nadpisValue = selectedOption.data('nadpis');
                    nadpis_nakleyki.text(nadpisValue)
                }
            }
        }        
        else{

            nakleyka.val('')
        }
        
        if(data_base[i]){
            clear_artikul(i)
        }
        
        });

    }
}

request_piece()

data_base = {}


function copy_tr(id){
    if(!data_base[id]){
        console.log('salom2222 copy')
    }else{
        
        text =""
        var size = $('#table-artikul tr').length;
        text = front_piece(start = size+1, end = size+2)
        var table = $('#table_tr'+id)
        var new_tr =$(text)

        table.after(new_tr)
        request_piece(start = size+1, end = size+2)
        
        var data = new BasePokritiya()

        for(key in data_base[id]){
            data[key] = data_base[id][key]
        }
       

        data_base[size+1] = data
        
        var s = size+1

        var id = data.id;
        var nazvaniye_system = data.nazvaniye_system;
        var base_artikul = data.base_artikul;
        var dlina = data.dlina;
        var splav = data.splav;
        var tip_zak = data.tip_zak;
        var combination = data.combination;
        var brend_kraska_sn = data.brend_kraska_sn;
        var kod_kraska_sn = data.kod_kraska_sn;
        var brend_kraska_vn = data.brend_kraska_vn;
        var kod_kraska_vn = data.kod_kraska_vn;
        var kod_dekor_sn = data.kod_dekor_sn;
        var svet_dekplonka_snaruji = data.svet_dekplonka_snaruji;
        var kod_dekor_vn = data.kod_dekor_vn;
        var svet_dekplonka_vnutri = data.svet_dekplonka_vnutri;

        var svet_lamplonka_snaruji = data.svet_lamplonka_snaruji;
        var kod_lam_sn = data.kod_lam_sn;
        var svet_lamplonka_vnutri = data.svet_lamplonka_vnutri;
        var kod_lam_vn = data.kod_lam_vn;


        var kod_anod_sn = data.kod_anod_sn;
        var kod_anod_vn = data.kod_anod_vn;


        var contactnost_anod = data.contactnost_anod;
        var tip_anod = data.tip_anod;
        var sposob_anod = data.sposob_anod;

        var kod_nakleyki = data.kod_nakleyki;
        var nadpis_nakleyki = data.nadpis_nakleyki;
        var baza_profiley = data.baza_profiley;
        
        

        var kratkiy_tekst = data.kratkiy_tekst;

        var sap_code_ruchnoy = data.sap_code;
        var kratkiy_text_ruchnoy = data.krat;
        
        var nazvaniye_ruchnoy = data.nazvaniye_ruchnoy
        var dilina_pressa = data.dilina_pressa

        var comment = data.comment;

        var is_termo = data.is_termo;


        var zavod = data.zavod
        var online_id = data.online_id
        var svet_product = data.svet_product
        var group_zakup = data.group_zakup
        var group = data.group
        var tip= data.tip
        var segment = data.segment
        var buxgalter_tovar = data.buxgalter_tovar
        var buxgalter_uchot = data.buxgalter_uchot
        var bazoviy_edin = data.bazoviy_edin
        var alter_edin = data.alter_edin
        var stoimost_baza = data.stoimost_baza
        var stoimost_alter = data.stoimost_alter
        var status_online = data.status_online
        var zavod_name = data.zavod_name
        var diller = data.diller
        var tip_clienta = data.tip_clienta 
        var is_active = data.is_active

        
        if(is_active){
            var icon = $('#icon_btn'+s)
            icon.children('i').remove()
            icon.append('<i class="bi bi-award-fill"></i>')
        }else{
            var icon = $('#icon_btn'+s)
            icon.children('i').remove()
            icon.append('<i class="bi bi-plus-circle"></i>')

        }
      
        var activate_btn =$('#activate_btn'+s);
        var create_btn =$('#create_btn'+s);
        activate_btn.css('display','none')
        create_btn.css('display','none')

        check_input_and_change(id,'#tip_pokritiya'+s)


        

        if(id ==1){
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=true)
            check_input_and_change('NT1','#nakleyka'+s,dis=true)
            check_text_and_change('БЕЗ НАКЛЕЙКИ','#nadpis_nakleyki'+s)

            if(is_termo){
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=true)
            }
        }else if(id == 2){    
                check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=true)
                check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=true)
                check_input_and_change(kod_nakleyki,'#nakleyka'+s)
                check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
                if(is_termo){
                    check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=true)
                    check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=true)
                }
        }else if(id ==3){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=false,is_req=true)
            check_input_and_change(kod_nakleyki,'#nakleyka'+s)
            check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)

            if(is_termo){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=false,is_req=true)
                check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
            }
        }
        else if(id ==4){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=false,is_req=true)

            check_input_and_change(kod_lam_sn,'#svet_lamplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_sn,'#code_lamplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_lam_vn,'#svet_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_text_and_change(kod_lam_vn,'#code_lamplonka_vnutri'+s,dis=false,is_req=true)
            check_input_and_change(kod_nakleyki,'#nakleyka'+s)
            check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
            if(is_termo){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=false,is_req=true)
            }

        }
        else if(id ==5){
            
            check_input_and_change(brend_kraska_sn,'#brand_k_snaruji'+s,dis=false,is_req=true)
            check_input_and_change(kod_kraska_sn,'#code_kraski_snar'+s,dis=false,is_req=true)

            check_input_and_change(svet_dekplonka_snaruji,'#svet_dekplonka_snaruji'+s,dis=false,is_req=true)
            check_text_and_change(svet_dekplonka_snaruji,'#code_dekplonka_snaruji'+s,dis=false,is_req=true)

            check_input_and_change(kod_nakleyki,'#nakleyka'+s)
            check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)

            if(is_termo){
                check_input_and_change(brend_kraska_vn,'#brand_k_vnutri'+s,dis=false,is_req=true)
                check_input_and_change(kod_kraska_vn,'#code_kraski_vnut'+s,dis=false,is_req=true)

                check_input_and_change(svet_dekplonka_vnutri,'#svet_dekplonka_vnutri'+s,dis=false,is_req=true)
                check_text_and_change(svet_dekplonka_vnutri,'#code_dekplonka_vnutri'+s,dis=false,is_req=true)
                check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)
            }

        }
        else if(id ==6){
            

            
            check_for_valid_and_set_val_select(kod_anod_sn,'code_svet_anodirovki_snaruji'+ s)

            check_input_and_change(contactnost_anod,'#contactnost_anodirovki'+s,dis=false,is_req=true)

            check_input_and_change(kod_nakleyki,'#nakleyka'+s)
            check_text_and_change(nadpis_nakleyki,'#nadpis_nakleyki'+s)

            get_anod(s)
            if(is_termo){
                check_for_valid_and_set_val_select(kod_anod_sn,'code_svet_anodirovki_vnutri'+ s)
                get_anod(s,is_termo=true)
            }



        }

       
        check_input_and_change(dlina,'#length'+s,dis=false,is_req=true)
        $('#artikul'+ s).attr('disabled',false)
        check_for_valid_and_set_val_select(base_artikul,'artikul'+ s,is_req=true)
        check_input_and_change(splav,'#splav'+s,dis=false,is_req=true)
        check_input_and_change(tip_zak,'#tip_zakalyonnosti'+s,dis=false,is_req=true)
        check_text_and_change(combination,'#combination'+s)
        check_text_and_change(nazvaniye_system,'.nazvaniye_system'+s)
        
        
        
        check_text_and_change(baza_profiley,'#baza_profiley'+s)
        
        check_text_and_change(kratkiy_tekst,'#kratkiy_tekst'+s)

        check_input_and_change(sap_code_ruchnoy,'#sap_code_ruchnoy'+s)
        check_input_and_change(kratkiy_text_ruchnoy,'#kratkiy_tekst_ruchnoy'+s)
        check_input_and_change(comment,'#comment'+s)
        check_input_and_change(dilina_pressa,'#dilina_pressa'+s)


       
        check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s)

        if(is_active){
            check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=false,is_req_simple=true)

            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod_name,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(diller,'#diller'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=false,is_req_simple=true)


        }else{
            check_input_and_change(zavod,'#zavod'+s,dis=false,is_req=true,is_req_simple=false)
            check_input_and_change(online_id,'#online_savdo_id'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(nazvaniye_ruchnoy,'#nazvaniye_ruchnoy'+s,dis=false,is_req=true)
            check_input_and_change(svet_product,'#svet_product'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(group_zakup,'#group_zakup'+s,dis=false,is_req=true,is_req_simple=false)

            check_input_and_change(group,'#group'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip,'#tip'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(segment,'#segment'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_tovar,'#buxgalter_tovar'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(buxgalter_uchot,'#buxgalter_uchot'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(bazoviy_edin,'#bazoviy_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(alter_edin,'#alter_edin'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_baza,'#stoimost_baza'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(stoimost_alter,'#stoimost_alter'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(status_online,'#status'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(zavod_name,'#zavod_name'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(diller,'#diller'+s,dis=false,is_req=false,is_req_simple=true)
            check_input_and_change(tip_clienta,'#tip_clienta'+s,dis=false,is_req=false,is_req_simple=true)

        }
        
        
    }


}

function check_for_valid_and_set_val_select(val,selector,is_req=false){
    if(is_req){
        var span = $('#select2-'+selector+'-container')
        span.css('display','block')
        span.css('border-color','red')

    }
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        ////// selec2 value change \\\\\\\
        var span = $('#select2-'+selector+'-container')
        span.attr('title',val);
        span.text(val);

        //////end ////////////
        
    }
}

function check_input_and_change(val,selector,dis=false,is_req=false,is_req_simple=false){
    if(is_req){
        
        $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','red')

    }
    if(is_req_simple){
        
        $(selector).attr('disabled',false)
        $(selector).css('display','block')
        $(selector).css('border-color','#dedad9')

    }
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        sel.attr('disabled',dis)
        sel.css('display','block')
        sel.css('border-color','#dedad9')
        sel.val(val)
        // console.log(val,typeof(val),selector)
    }
    
}

function check_text_and_change(val,selector){
    if(val !=NaN && val !='' && String(val) != 'NaN'){
        var sel = $(selector)
        sel.css('display','block')
        sel.text(val)
    }
}

function create(i){
    
    var artikul = $('#artikul'+i)
    
    artikul.attr('disabled',false)

    var status_first =$('#status'+i);
    status_first.val('Пассивный')
    // status_first.attr('disabled',true)


    var tip =$('#tip'+i);
    tip.val('Готовый продукт')
    

    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    activate_btn.css('display','none')
    create_btn.css('display','none')

    var icon = $('#icon_btn'+i)
    icon.children('i').remove()
    icon.append('<i class="bi bi-plus-circle"></i>')    
   
}

function activate(i){
    // data_base[i] = new OnlineSavdo()

    var artikul = $('#artikul'+i)
    
    artikul.attr('disabled',false)


    var activate_btn =$('#activate_btn'+i);
    var create_btn =$('#create_btn'+i);
    activate_btn.css('display','none')
    create_btn.css('display','none')
    var status_first =$('#status'+i);
    status_first.val('Активный')
    // status_first.attr('disabled',true)
    var icon = $('#icon_btn'+i)
    icon.children('i').remove()
    icon.append('<i class="bi bi-award-fill"></i>')

}



function get_anod(termo=false){
    $('.kod_anod_snar').select2({
        ajax: {
            url: "/client/client-anod-list",
            dataType: 'json',
            processResults: function(data){
                return {results: $.map(data, function(item){
                    return {id:item.id,text:item.code_sveta,tip_anod:item.tip_anod,sposob_anod:item.sposob_anod}
                })
            };
            }
        }
        });
    if (termo){
        $('.kod_anod_vnutri').select2({
            ajax: {
                url: "/client/client-anod-list",
                dataType: 'json',
                processResults: function(data){
                    return {results: $.map(data, function(item){
                        return {id:item.id,text:item.code_sveta,tip_anod:item.tip_anod,sposob_anod:item.sposob_anod}
                    })
                };
                }
            }
            });
    }
}



function clear_artikul(id){

    if(data_base[id]){
        var is_termo = data_base[id].is_termo
        var base_artikul =$('#select2-artikul'+id+'-container').text()
        var nazvaniye_system = $('.nazvaniye_system'+id).text()
        var combination =$('#combination'+id).text()
        var baza_profiley =$('#baza_profiley'+id).text()
  

        data_base[id].base_artikul = base_artikul
        data_base[id].nazvaniye_system = nazvaniye_system
        data_base[id].combination = combination
        data_base[id].baza_profiley = baza_profiley

        
        var sss= combination.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'
    
        if (sss){
            var second_is_termo = false
        }else{
            var second_is_termo = true
        }

        if(is_termo != second_is_termo){
         


            var table_tr =$('#table_tr'+id);
            // $('.nazvaniye_system'+id).text('');
            var tip_pokritiya = $('#tip_pokritiya'+String(id));
            tip_pokritiya.val('0').change();

            delete data_base[id]

            var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
            kratkiy_tekst.innerText="";


            
            
            table_tr.css('background-color','white')
            

            var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
            code_kraski_snaruji.val("");
            code_kraski_vnutri.val("");
            brand_kraski_vnutri.val("");
            brand_kraski_snaruji.val("");

            code_kraski_snaruji.css("border-color",'#dedad9');
            code_kraski_vnutri.css("border-color",'#dedad9');
            brand_kraski_vnutri.css("border-color",'#dedad9');
            brand_kraski_snaruji.css("border-color",'#dedad9');



            var dlina =$('#length'+String(id));
            dlina.val('');
            dlina.attr("disabled",true);
            dlina.css("border-color",'#dedad9');

            var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
            svet_lamplonka_snaruji.val('0').change();
            svet_lamplonka_snaruji.attr("disabled",true);
            svet_lamplonka_snaruji.css("border-color",'#dedad9');
            var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
            code_lamplonka_snaruji.text("")
            

            var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
            svet_lamplonka_vnutri.val('0').change();
            svet_lamplonka_vnutri.attr("disabled",true);
            svet_lamplonka_vnutri.css("border-color",'#dedad9');
            var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
            code_lamplonka_vnutri.text("")

            var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
            var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id))

            if(nakleyka_codd != ''){
                var nakleyka = $('#nakleyka'+String(id))
                nakleyka.css('display','block')
                nakleyka.attr('disabled',false)
                nakleyka.val(nakleyka_codd)

                var selectedOption = $('#nakleyka'+String(id)).find('option:selected');
                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)
            }else{
                var nakleyka = $('#nakleyka'+String(id))
                nakleyka.css('display','block')
                nakleyka.attr('disabled',false)
                nakleyka.val('')

                var selectedOption = $('#nakleyka'+String(id)).find('option:selected');
                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)

            }


            var splav = $('#splav'+String(id));
            splav.val('0').change();
            splav.attr("disabled",true);
            splav.css("border-color",'#dedad9');
            var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
            tip_zakalyonnosti.val('0').change();
            tip_zakalyonnosti.attr("disabled",true);
            tip_zakalyonnosti.css("border-color",'#dedad9');

        }
    }
    
}

function artukil_clear(id){
    $('#artikul'+id).val(null).trigger('change');
    var table_tr =$('#table_tr'+id);
    $('.nazvaniye_system'+id).text('');
    var tip_pokritiya = $('#tip_pokritiya'+String(id));
    tip_pokritiya.val('0').change();
    tip_pokritiya.attr("disabled",true);
    delete data_base[id]

    var kratkiy_tekst = document.getElementById('kratkiy_tekst'+String(id));
    kratkiy_tekst.innerText="";


    var icon = $('#icon_btn'+id)
    icon.children('i').remove()
    icon.append('<i class="bi bi-three-dots-vertical"></i>')
    
    table_tr.css('background-color','white')
    

    var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
    var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
    code_kraski_snaruji.val("");
    code_kraski_vnutri.val("");
    brand_kraski_vnutri.val("");
    brand_kraski_snaruji.val("");

    code_kraski_snaruji.css("border-color",'#dedad9');
    code_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_snaruji.css("border-color",'#dedad9');



    var dlina =$('#length'+String(id));
    dlina.val('');
    dlina.attr("disabled",true);
    dlina.css("border-color",'#dedad9');

    var combination= $('#combination'+String(id));
    combination.text("");

    var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
    svet_lamplonka_snaruji.val('0').change();
    svet_lamplonka_snaruji.attr("disabled",true);
    svet_lamplonka_snaruji.css("border-color",'#dedad9');
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text("")
    

    var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
    svet_lamplonka_vnutri.val('0').change();
    svet_lamplonka_vnutri.attr("disabled",true);
    svet_lamplonka_vnutri.css("border-color",'#dedad9');
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text("")

    var nakleyka = $('#nakleyka'+String(id))
    nakleyka.css('display','none')
    nakleyka.val('')


    var splav = $('#splav'+String(id));
    splav.val('0').change();
    splav.attr("disabled",true);
    splav.css("border-color",'#dedad9');
    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    tip_zakalyonnosti.val('0').change();
    tip_zakalyonnosti.attr("disabled",true);
    tip_zakalyonnosti.css("border-color",'#dedad9');

    $('#artikul'+id).attr('disabled',true)

    var status_first = $('#status'+String(id))
    // status_first.attr('disabled',false)
    status_first.val('Активный')

    var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
    var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
    var online_savdo_id =$('#online_savdo_id'+id);
    var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);


    var svet_product =$('#svet_product'+id);
    var group_zakup =$('#group_zakup'+id);
    var group =$('#group'+id);
    var tip =$('#tip'+id);
    var bazoviy_edin =$('#bazoviy_edin'+id);
    var status =$('#status'+id);
    var zavod =$('#zavod'+id);
    var buxgalter_uchot =$('#buxgalter_uchot'+id);
    var alter_edin =$('#alter_edin'+id);
    var stoimost_baza =$('#stoimost_baza'+id);
    var stoimost_alter =$('#stoimost_alter'+id);
    var segment =$('#segment'+id);
    var buxgalter_tovar =$('#buxgalter_tovar'+id);
    var zavod_name =$('#zavod_name'+id)
    zavod_name.text('')


    svet_product.css('display','none')
    group_zakup.css('display','none')
    group.css('display','none')
    tip.css('display','none')
    bazoviy_edin.css('display','none')
    status.css('display','none')
    zavod.css('display','none')
    buxgalter_uchot.css('display','none')
    alter_edin.css('display','none')
    stoimost_baza.css('display','none')
    stoimost_alter.css('display','none')
    segment.css('display','none')
    buxgalter_tovar.css('display','none')
    sap_code_ruchnoy.css('display','none')
    kratkiy_tekst_ruchnoy.css('display','none')
    online_savdo_id.css('display','none')
    online_savdo_id.css('border-color','red')
    nazvaniye_ruchnoy.css('display','none')
    nazvaniye_ruchnoy.css('border-color','red')


    svet_product.css('border-color','red')
    group_zakup.css('border-color','red')
    group.css('border-color','red')
    tip.css('border-color','red')
    bazoviy_edin.css('border-color','red')
    status.css('border-color','red')
    zavod.css('border-color','red')

    
    sap_code_ruchnoy.val('')
    kratkiy_tekst_ruchnoy.val('')
    online_savdo_id.val('')
    nazvaniye_ruchnoy.val('')
    svet_product.val('')
    group_zakup.val('')
    group.val('')
    tip.val('')
    bazoviy_edin.val('')
    status.val('Активный')
    zavod.val('')
    buxgalter_uchot.val('')
    alter_edin.val('')
    stoimost_baza.val('')
    stoimost_alter.val('')
    segment.val('')
    buxgalter_tovar.val('')
    
    var create_btn =$('#create_btn'+id);
    var activate_btn =$('#activate_btn'+id);

    activate_btn.css('display','block')
    create_btn.css('display','block')



}


function tip_pokritiya_selected(id,val){

    var element33 = document.getElementById("table_tr"+id);
    element33.style.backgroundColor='white';
    
    
    var select_anod_snar = $('#anod'+String(id));
    select_anod_snar.children("span").css('display','none');

    var dlina =$('#length'+String(id));
    dlina.attr("disabled",false);
    dlina.css("border-color",'#fc2003');

    var select_anod_vnut = $('#anod_vnutr'+String(id));
    select_anod_vnut.children("span").css('display','none');
    
    var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
    var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
    var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
    var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    kratkiy_tekst.text("");
    code_kraski_snaruji.val("");
    code_kraski_vnutri.val("");
    brand_kraski_vnutri.val("");
    brand_kraski_snaruji.val("");

    code_kraski_snaruji.css("border-color",'#dedad9');
    code_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_vnutri.css("border-color",'#dedad9');
    brand_kraski_snaruji.css("border-color",'#dedad9');

    code_kraski_snaruji.css("display",'none');
    code_kraski_vnutri.css("display",'none');
    brand_kraski_vnutri.css("display",'none');
    brand_kraski_snaruji.css("display",'none');


    var combination= $('#combination'+String(id));
    combination_text = combination.text();
  

    var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
    svet_lamplonka_snaruji.val('0').change();
    svet_lamplonka_snaruji.attr("disabled",true);
    svet_lamplonka_snaruji.css("border-color",'#dedad9');
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text("")
    code_lamplonka_snaruji.css("border-color",'#dedad9');

    var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
    svet_lamplonka_vnutri.val('0').change();
    svet_lamplonka_vnutri.attr("disabled",true);
    svet_lamplonka_vnutri.css("border-color",'#dedad9');
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text("")
    code_lamplonka_vnutri.css("border-color",'#dedad9');

    var svet_dekplonka_snaruji = $('#svet_dekplonka_snaruji'+String(id));
    svet_dekplonka_snaruji.val('0').change();
    svet_dekplonka_snaruji.attr("disabled",true);
    svet_dekplonka_snaruji.css("border-color",'#dedad9');

    var code_dekplonka_snaruji = $('#code_dekplonka_snaruji'+String(id));
    code_dekplonka_snaruji.text("");
    code_dekplonka_snaruji.css("border-color",'#dedad9');

    var svet_dekplonka_vnutri = $('#svet_dekplonka_vnutri'+String(id));
    svet_dekplonka_vnutri.val('0').change();
    svet_dekplonka_vnutri.attr("disabled",true);
    svet_dekplonka_vnutri.css("border-color",'#dedad9');
    var code_dekplonka_vnutri = $('#code_dekplonka_vnutri'+String(id));
    code_dekplonka_vnutri.text("");
    code_dekplonka_vnutri.css("border-color",'#dedad9');

    var code_svet_anodirovki_vnutri = $('#code_svet_anodirovki_vnutri'+String(id));
    code_svet_anodirovki_vnutri.val('0').change();
    code_svet_anodirovki_vnutri.attr("disabled",true);
    code_svet_anodirovki_vnutri.css("border-color",'#dedad9');
    
    var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
    if(data_base[id]){
        contactnost_anodirovki.val('0').change();
    }
    contactnost_anodirovki.attr("disabled",true);
    contactnost_anodirovki.css("border-color",'#dedad9');


    var splav = $('#splav'+String(id));
    // console.log(splav,'splavvvv')
    splav.attr("disabled",false);
    splav.val('63')
    splav.css("border-color","#fc2003");
    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    tip_zakalyonnosti.attr("disabled",false);
    tip_zakalyonnosti.css("border-color","#fc2003");





    var tip_anodirovki =$('#tip_anodirovki'+String(id));
    var sposob_anodirovki = $('#sposob_anodirovki'+String(id));
    
    tip_anodirovki.text("");
    sposob_anodirovki.text("")
    var nakleyka = $('#nakleyka'+String(id))

    var status_first = $('#status'+String(id))
    var svet_product_val =''

    if(String(val) == '1'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 1
        data_base[id].tip_pokritiya = 'Неокрашенный'
        nakleyka.css('display','block');
        nakleyka.val("NT1");
        
        svet_product_val = 'Без цвета'
       
        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id))
            code_kraski_snaruji.val('MF')
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            code_kraski_snaruji.val('MF');
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')
            
            code_kraski_vnutri.val('MF');
            code_kraski_vnutri.attr('disabled',true)
            code_kraski_vnutri.css('display','block')
            code_kraski_vnutri.css('border-color','#dedad9')
        }

    }else if(String(val) == '2'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 2
        data_base[id].tip_pokritiya = 'Белый'
        svet_product_val = 'WHITE'

        if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))
        
            code_kraski_snaruji.val('9016');
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')

            brand_kraski_snaruji.val('R');
            brand_kraski_snaruji.attr('disabled',true)
            brand_kraski_snaruji.css('display','block')
            brand_kraski_snaruji.css('border-color','#dedad9')
        }else{
            var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id))
            var brand_kraski_snaruji = $('#brand_k_snaruji'+String(id))

            brand_kraski_snaruji.val('R');
            brand_kraski_snaruji.attr('disabled',true)
            brand_kraski_snaruji.css('display','block')
            brand_kraski_snaruji.css('border-color','#dedad9')

            code_kraski_snaruji.val('9016');
            code_kraski_snaruji.attr('disabled',true)
            code_kraski_snaruji.css('display','block')
            code_kraski_snaruji.css('border-color','#dedad9')

            brand_kraski_vnutri.val('R');
            brand_kraski_vnutri.attr('disabled',true)
            brand_kraski_vnutri.css('display','block')
            brand_kraski_vnutri.css('border-color','#dedad9')

            code_kraski_vnutri.val('9016');
            code_kraski_vnutri.attr('disabled',true)
            code_kraski_vnutri.css('display','block')
            code_kraski_vnutri.css('border-color','#dedad9')

        }

        
        
        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }
            
    }else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){

        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }

        if(String(val) == '3'){
            data_base[id] = new BasePokritiya()
            data_base[id].id = 3
            data_base[id].tip_pokritiya = 'Окрашенный'
            svet_product_val ='COLOUR'
        }else if(String(val) == '4'){
            data_base[id] = new BasePokritiya()
            data_base[id].tip_pokritiya = 'Ламинированный'
            data_base[id].id = 4
            svet_product_val ='LAM'
        }else if(String(val) == '5'){
            data_base[id] = new BasePokritiya()
            data_base[id].id = 5
            data_base[id].tip_pokritiya = 'Сублимированный'
            svet_product_val ='VAKUM & 3D'
        } 
        
        
       
        var brand_k_snaruji = $('#brand_k_snaruji'+String(id));
        brand_k_snaruji.attr('disabled',false)
        brand_k_snaruji.css('display','block')
        var code_kraski_snar = $('#code_kraski_snar'+String(id));
        code_kraski_snar.attr('disabled',false)
        code_kraski_snar.css('display','block')
       
        
        
       

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            
            var brand_kraski_vnutri = $('#brand_k_vnutri'+String(id));
            brand_kraski_vnutri.attr('disabled',false)
            brand_kraski_vnutri.css('display','block')
            var code_kraski_vnutri = $('#code_kraski_vnut'+String(id));
            code_kraski_vnutri.attr('disabled',false)
            code_kraski_vnutri.css('display','block')

        }

        if (String(val) == '4'){
            var svet_lamplonka_snaruji = $('#svet_lamplonka_snaruji'+String(id));
            svet_lamplonka_snaruji.attr("disabled",false);
            svet_lamplonka_snaruji.attr("required",true);
            svet_lamplonka_snaruji.css("border-color",'#fc2003');
            var svet_lamplonka_vnutri = $('#svet_lamplonka_vnutri'+String(id));
            svet_lamplonka_vnutri.attr("disabled",false);
            svet_lamplonka_vnutri.attr("required",true);
            svet_lamplonka_vnutri.css("border-color",'#fc2003');

            
        }

        if (String(val) == '5'){
            
            var svet_dekplonka_snaruji = $('#svet_dekplonka_snaruji'+String(id));
            svet_dekplonka_snaruji.attr("disabled",false);
            svet_dekplonka_snaruji.attr("required",true);
            svet_dekplonka_snaruji.css("border-color",'#fc2003');
           
            if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
                var svet_dekplonka_vnutri = $('#svet_dekplonka_vnutri'+String(id));
                svet_dekplonka_vnutri.attr("disabled",false);
                svet_dekplonka_vnutri.attr("required",true);
                svet_dekplonka_vnutri.css("border-color",'#fc2003');
            }
            
        }
        

    }else if(String(val) == '6'){
        data_base[id] = new BasePokritiya()
        data_base[id].id = 6
        data_base[id].tip_pokritiya = 'Анодированный'
        svet_product_val ='Anod'
        

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){ 
            get_anod(id,termo=true)

            var code_svet_anodirovki_vnutri = $('#code_svet_anodirovki_vnutri'+String(id));
            code_svet_anodirovki_vnutri.attr("disabled",false);
            code_svet_anodirovki_vnutri.attr("required",true);
            code_svet_anodirovki_vnutri.css("border-color",'#fc2003');

        }else{
            get_anod(id,termo=false)
            
        }

        

        var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
        console.log(contactnost_anodirovki)
        contactnost_anodirovki.attr("disabled",false);
        contactnost_anodirovki.attr("required",true);
        contactnost_anodirovki.css("border-color",'red');

        
        var nakleyka_codd = $('#nakleyka_codd'+String(id)).text()
        if(nakleyka_codd!=''){
            nakleyka.val(nakleyka_codd)
        }
        
        
        
    }
    
    if(String(val) != ''){
        var base_artikul =$('#select2-artikul'+id+'-container')
        var nazvaniye_system = $('.nazvaniye_system'+id).text()
        var combination =$('#combination'+id).text()
        data_base[id].nazvaniye_system = nazvaniye_system;
        data_base[id].combination = combination;
        data_base[id].base_artikul = base_artikul.text()
        var baza_profiley =$('#baza_profiley'+id)
        var gruppa_materialov =$('#gruppa_materialov'+id)
        var comment =$('#comment'+id)
        data_base[id].baza_profiley = baza_profiley.text()
        data_base[id].gruppa_materialov = gruppa_materialov.text()
        data_base[id].comment = comment.val()
        
        var nadpis_nakleyki =$('#nadpis_nakleyki'+id)
        
        if(nadpis_nakleyki!=''){
            data_base[id].nadpis_nakleyki = nadpis_nakleyki.text()
        }

    }


    if(status_first.val()=='Активный' && String(val) != ''){
        console.log(status_first.val())
        
        data_base[id].is_active=true

        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
        var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod'+id);
        var buxgalter_uchot =$('#buxgalter_uchot'+id);
        var alter_edin =$('#alter_edin'+id);
        var stoimost_baza =$('#stoimost_baza'+id);
        var stoimost_alter =$('#stoimost_alter'+id);
        var segment =$('#segment'+id);
        var buxgalter_tovar =$('#buxgalter_tovar'+id);
    
        
        
        
        
        sap_code_ruchnoy.css('display','block')
        kratkiy_tekst_ruchnoy.css('display','block')
        online_savdo_id.css('display','block')
        nazvaniye_ruchnoy.css('display','block')
        svet_product.css('display','block')
        group_zakup.css('display','block')
        group.css('display','block')
        tip.css('display','block')
        bazoviy_edin.css('display','block')
        status.css('display','block')
        zavod.css('display','block')
        buxgalter_uchot.css('display','block')
        alter_edin.css('display','block')
        stoimost_baza.css('display','block')
        stoimost_alter.css('display','block')
        segment.css('display','block')
        buxgalter_tovar.css('display','block')


        status.val('Активный')
        data_base[id].status_name='Активный'
        // status.attr('disabled',true)

        sap_code_ruchnoy.css('border-color','#dedad9')
        kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
        online_savdo_id.css('border-color','#dedad9')
        nazvaniye_ruchnoy.css('border-color','#dedad9')
        svet_product.css('border-color','#dedad9')
        group_zakup.css('border-color','#dedad9')
        group.css('border-color','#dedad9')
        tip.css('border-color','#dedad9')
        bazoviy_edin.css('border-color','#dedad9')
        status.css('border-color','#dedad9')
        zavod.css('border-color','#dedad9')
        buxgalter_uchot.css('border-color','#dedad9')
        alter_edin.css('border-color','#dedad9')
        stoimost_baza.css('border-color','#dedad9')
        stoimost_alter.css('border-color','#dedad9')
        segment.css('border-color','#dedad9')
        buxgalter_tovar.css('border-color','#dedad9')
    }else if(status_first.val()=='Пассивный' && String(val) != ''){
        console.log(status_first.val())
        var svet_product =$('#svet_product'+id);
        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
        var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod'+id);
        var buxgalter_uchot =$('#buxgalter_uchot'+id);
        var alter_edin =$('#alter_edin'+id);
        var stoimost_baza =$('#stoimost_baza'+id);
        var stoimost_alter =$('#stoimost_alter'+id);
        var segment =$('#segment'+id);
        var buxgalter_tovar =$('#buxgalter_tovar'+id);
        
        svet_product.val(svet_product_val)
        data_base[id].svet_product=svet_product_val
        data_base[id].tip='Готовый продукт'
        data_base[id].buxgalter_uchot='Килограмм'
        data_base[id].bazoviy_edin='Штука'
        data_base[id].alter_edin='Килограмм'
        data_base[id].stoimost_baza='1'
        
        buxgalter_uchot.val('Килограмм')
        bazoviy_edin.val('Штука')
        alter_edin.val('Килограмм')
        stoimost_baza.val('1')
        
        sap_code_ruchnoy.css('display','block')
        kratkiy_tekst_ruchnoy.css('display','block')
        online_savdo_id.css('display','block')
        nazvaniye_ruchnoy.css('display','block')
        svet_product.css('display','block')
        group_zakup.css('display','block')
        group.css('display','block')
        tip.css('display','block')
        bazoviy_edin.css('display','block')
        status.css('display','block')
        zavod.css('display','block')
        buxgalter_uchot.css('display','block')
        alter_edin.css('display','block')
        stoimost_baza.css('display','block')
        stoimost_alter.css('display','block')
        segment.css('display','block')
        buxgalter_tovar.css('display','block')
        
        status.val('Пассивный')
        data_base[id].status_name='Пассивный'
        // status.attr('disabled',true)

        online_savdo_id.css('border-color','#dedad9')

    }

    create_kratkiy_tekst(id);
}


function code_svet_anodirovki_snaruji_selected(id,val){
    $("#code_svet_anodirovki_snaruji"+String(id)).on("select2:select", function (e) { 
    
        var tip_anodirovki =$('#tip_anodirovki'+String(id));
        var sposob_anodirovki = $('#sposob_anodirovki'+String(id));
        console.log(e.params.data.text);
        tip_anodirovki.text(e.params.data.tip_anod);
        sposob_anodirovki.text(e.params.data.sposob_anod);

        var selectedOption = $(this).find(':selected');
            $(this).siblings('.select2-container').find('.select2-selection--single').css('border-color', '#000');
    
    
    });
    if (val !=''){
        create_kratkiy_tekst(id);
    }

}

function svet_lamplonka_snaruji_selected(id,val){
    var code_lamplonka_snaruji = $('#code_lamplonka_snaruji'+String(id));
    code_lamplonka_snaruji.text(String(val))
    
    var svet_lamplonka_snaruji = document.getElementById('svet_lamplonka_snaruji'+String(id))
    svet_lamplonka_snaruji.style.borderColor='red';
    // data_base[id].kod_lam_sn =NaN;
    create_kratkiy_tekst(id);
    

}
function svet_lamplonka_vnutri_selected(id,val){
    var code_lamplonka_vnutri = $('#code_lamplonka_vnutri'+String(id));
    code_lamplonka_vnutri.text(String(val));
    var svet_lamplonka_vnutri = document.getElementById('svet_lamplonka_vnutri'+String(id))
    svet_lamplonka_vnutri.style.borderColor='red';
    create_kratkiy_tekst(id);
    
}


function svet_dekplonka_snaruji_selected(id,val){
    var code_dekplonka_snaruji = $('#code_dekplonka_snaruji'+String(id));
    code_dekplonka_snaruji.text(String(val))
    var selectElement = document.getElementById('svet_dekplonka_snaruji'+String(id));
    selectElement.style.borderColor='red';
    create_kratkiy_tekst(id);
    
}
function svet_dekplonka_vnutri_selected(id,val){
    var code_dekplonka_vnutri = $('#code_dekplonka_vnutri'+String(id));
    code_dekplonka_vnutri.text(String(val));
    var selectElement = document.getElementById('svet_dekplonka_vnutri'+String(id));
    selectElement.style.borderColor='red';
    create_kratkiy_tekst(id);
}

var zapros_count =[]



function create_kratkiy_tekst(id){
    if(!data_base[id]){
        console.log('salom')
    }else{
    
    var kratkiy_tekst = $('#kratkiy_tekst'+String(id));
    var combination= $('#combination'+String(id));
    var comment= $('#comment'+String(id));
    combination_text = combination.text();
    comment = comment.val();
    var val = $('#tip_pokritiya'+String(id)).val();
    var dlina = $('#length'+String(id));

    
    if(comment!=''){
        data_base[id].comment = comment;
    }else{
        data_base[id].comment = NaN;
    }
    if(dlina.val()!=''){
        dlina.css("border-color",'#dedad9');
        data_base[id].dlina = dlina.val();
    }else{
        dlina.css("border-color",'red');
        data_base[id].dlina = NaN;
    }
    var dilina_pressa = $('#dilina_pressa'+String(id));
    if(dilina_pressa.val()!=''){
        dilina_pressa.css("border-color",'#dedad9');
        data_base[id].dilina_pressa = dilina_pressa.val();
    }else{
        data_base[id].dilina_pressa = NaN;
    }
    
    var splav = $('#splav'+String(id));
    if(splav){
        if(splav.val()!='0' && splav.val()!='' && splav.val()!=null){
            splav.css("border-color",'#dedad9');
            data_base[id].splav = splav.val();
        }else{
            splav.css("border-color",'red');
            data_base[id].splav = NaN;
        }
    }

    var tip_zakalyonnosti = $('#tip_zakalyonnosti'+String(id));
    if(tip_zakalyonnosti){
        if(tip_zakalyonnosti.val()!='0' && tip_zakalyonnosti.val()!='' && tip_zakalyonnosti.val()!=null){
            tip_zakalyonnosti.css("border-color",'#dedad9');
            data_base[id].tip_zak = tip_zakalyonnosti.val();
        }else{
            tip_zakalyonnosti.css("border-color",'red');
            data_base[id].tip_zak = NaN;
        }
    }
    var nakleyka = $('#nakleyka'+String(id))
    var nadpis_nakleyki = $('#nadpis_nakleyki'+String(id))

    if(String(val) == '1'){
            
            data_base[id].kod_kraska_sn = 'MF'
            data_base[id].kod_nakleyki = 'NT1'
            data_base[id].nadpis_nakleyki = 'Без наклейки'
            var nakleyka = $('#nakleyka'+String(id))
            nadpis_nakleyki.text('Без наклейки')
            nakleyka.attr('disabled',true)
            nakleyka.val('NT1')
        
         if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {
                
                data_base[id].kod_kraska_vn = 'MF'
                data_base[id].is_termo = true;
                
            }

    }else if(String(val) == '2'){
        data_base[id].brend_kraska_sn ='R'
        data_base[id].kod_kraska_sn ='9016'

        var nakleyka = $('#nakleyka'+String(id))
        nakleyka.attr('disabled',false)
        if(nakleyka.val()!=''){
            data_base[id].kod_nakleyki = nakleyka.val();
            var selectedOption = $('#nakleyka'+String(id)).find('option:selected');

            var nadpisValue = selectedOption.data('nadpis');
            nadpis_nakleyki.text(nadpisValue)
            nakleyka.css('border-color','#dedad9')
        }else{
            data_base[id].kod_nakleyki = NaN;
            nadpis_nakleyki.text('')
            nakleyka.css('border-color','red')
        }

        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {

                data_base[id].brend_kraska_vn = 'R';
                data_base[id].kod_kraska_vn = '9016';
                data_base[id].is_termo = true
            }
    }
    else if(String(val) == '3' || String(val) == '4'|| String(val) == '5'){
        
        var brend_kraska_sn = $('#brand_k_snaruji'+String(id))
        if(brend_kraska_sn.val() != '0' && brend_kraska_sn.val()  != undefined && brend_kraska_sn.val()  !=null){
            brend_kraska_sn.css("border-color",'#dedad9');
            data_base[id].brend_kraska_sn =brend_kraska_sn.val();
        }else{
            brend_kraska_sn.css("border-color",'red');
            data_base[id].brend_kraska_sn =NaN;
        }
        
        var code_kraski_snaruji = $('#code_kraski_snar'+String(id));
        if(code_kraski_snaruji.val() != '0' && code_kraski_snaruji.val()  != undefined && code_kraski_snaruji.val() != '' && code_kraski_snaruji.val()  !=null){
            code_kraski_snaruji.css("border-color",'#dedad9');
            data_base[id].kod_kraska_sn =code_kraski_snaruji.val();
        }else{
            code_kraski_snaruji.css("border-color",'red');
            data_base[id].kod_kraska_sn =NaN;
        }
       
       


        if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {

                var brend_kraska_vn = $('#brand_k_vnutri'+String(id))
                if(brend_kraska_vn.val() != '0' && brend_kraska_vn.val()  != undefined && brend_kraska_vn.val()  != null){
                    brend_kraska_vn.css("border-color",'#dedad9');
                    data_base[id].brend_kraska_vn =brend_kraska_vn.val();
                }else{
                    brend_kraska_vn.css("border-color",'red');
                    data_base[id].brend_kraska_vn =NaN;
                }

                var code_kraski_vnut = $('#code_kraski_vnut'+String(id))
                if(code_kraski_vnut.val() != '0' && code_kraski_vnut.val()  != undefined && code_kraski_vnut.val()  != '' && code_kraski_vnut.val()  !=null){
                    code_kraski_vnut.css("border-color",'#dedad9');
                    data_base[id].kod_kraska_vn =code_kraski_vnut.val();
                }else{
                    code_kraski_vnut.css("border-color",'red');
                    data_base[id].kod_kraska_vn =NaN;
                }

                data_base[id].is_termo =true;
                
            }



            var nakleyka = $('#nakleyka'+String(id))
            nakleyka.attr('disabled',false)
            if(nakleyka.val()!=''){
                data_base[id].kod_nakleyki = nakleyka.val();
                var selectedOption = $('#nakleyka'+String(id)).find('option:selected');
    
                var nadpisValue = selectedOption.data('nadpis');
                nadpis_nakleyki.text(nadpisValue)
                nakleyka.css('border-color','#dedad9')
            }else{
                data_base[id].kod_nakleyki = NaN;
                nadpis_nakleyki.text('')
                nakleyka.css('border-color','red')
            }

       
        if(String(val) == '4'){
            
            var code_lamplonka_snaruji = document.getElementById('code_lamplonka_snaruji'+String(id))//.innerText;
            
            if(code_lamplonka_snaruji.innerText !=''){
                var svet_lamplonka_snaruji = document.getElementById('svet_lamplonka_snaruji'+String(id))//.innerText;
                svet_lamplonka_snaruji.style.borderColor='#dedad9';
                data_base[id].kod_lam_sn =code_lamplonka_snaruji.innerText;
                var svet_lamplonka_sn = $('#svet_lamplonka_snaruji'+String(id)+' option:selected').text()
                data_base[id].svet_lamplonka_snaruji =svet_lamplonka_sn;
                
            }else{
                data_base[id].svet_lamplonka_snaruji =NaN;
                data_base[id].kod_lam_sn =NaN;
            }
            
            var code_lamplonka_vnutri = document.getElementById('code_lamplonka_vnutri'+String(id));
           

            if(code_lamplonka_vnutri.innerText !=''){
                var svet_lamplonka_vnutri = document.getElementById('svet_lamplonka_vnutri'+String(id))//.innerText;
                svet_lamplonka_vnutri.style.borderColor='#dedad9';
                
                data_base[id].kod_lam_vn =code_lamplonka_vnutri.innerText;
                var svet_lamplonka_vn = $('#svet_lamplonka_vnutri'+String(id)+' option:selected').text()
                data_base[id].svet_lamplonka_vnutri =svet_lamplonka_vn;
            }else{
                data_base[id].svet_lamplonka_vnutri = NaN;
                data_base[id].kod_lam_vn = NaN;
            }

        }
        if(String(val) == '5'){
            var selectElement = document.getElementById('svet_dekplonka_snaruji'+String(id));

            var selectedIndex = selectElement.selectedIndex;
            if(selectedIndex !=-1){
                selectElement.style.borderColor='#dedad9';
                var selectedOption = selectElement.options[selectedIndex];
                var selectedText = selectedOption.textContent;
                
                if (selectedText!=''){
                    var svet_dekplonka_sn =$('#code_dekplonka_snaruji'+id).text()
                    data_base[id].svet_dekplonka_snaruji =svet_dekplonka_sn;
                    data_base[id].kod_dekor_sn =selectedText;
                }else{
                    selectElement.style.borderColor='red';
                    data_base[id].svet_dekplonka_snaruji =NaN;
                    data_base[id].kod_dekor_sn =NaN;
                }
            }else{
                data_base[id].svet_dekplonka_snaruji =NaN;
                data_base[id].kod_dekor_sn =NaN;
            }

            if (combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА')
            {
                var selectElement = document.getElementById('svet_dekplonka_vnutri'+String(id));

                var selectedIndex = selectElement.selectedIndex;
                if(selectedIndex !=-1){
                    selectElement.style.borderColor='#dedad9';
                    var selectedOption = selectElement.options[selectedIndex];
                    var selectedText = selectedOption.textContent;
                    data_base[id].kod_dekor_vn =selectedText;
                    if (selectedText!=''){
                        var svet_dekplonka_vn =$('#code_dekplonka_vnutri'+id).text()
                        data_base[id].svet_dekplonka_vnutri =svet_dekplonka_vn;
                        data_base[id].kod_dekor_vn =selectedText;
                    }else{
                        selectElement.style.borderColor='red';
                        data_base[id].svet_dekplonka_vnutri =NaN;
                        data_base[id].kod_dekor_vn =NaN;
                    }
                }else{
                    data_base[id].svet_dekplonka_vnutri =NaN;
                    selectElement.style.borderColor='red';
                    data_base[id].kod_dekor_vn =NaN;
                }
            }
            // this.kod_dekor_sn && this.kod_dekor_vn

        }

    }else if(String(val) == '6'){
        var nakleyka = $('#nakleyka'+String(id))
        nakleyka.attr('disabled',false)
        if(nakleyka.val()!=''){
            data_base[id].kod_nakleyki = nakleyka.val();
            var selectedOption = $('#nakleyka'+String(id)).find('option:selected');

            var nadpisValue = selectedOption.data('nadpis');
            nadpis_nakleyki.text(nadpisValue)
            nakleyka.css('border-color','#dedad9')
        }else{
            data_base[id].kod_nakleyki = NaN;
            nadpis_nakleyki.text('')
            nakleyka.css('border-color','red')
        }

        var anod_sn = document.getElementById("anod"+String(id))
        const spanTextbox1 = anod_sn.querySelector('span[role="textbox"]');
        
        const spanss =document.querySelector('#anod'+String(id) +' .select2-container .select2-selection--single')
        if(spanTextbox1){
            if(spanTextbox1.innerText !='' ){
                spanss.style.borderColor='#dedad9';
                data_base[id].kod_anod_sn = spanTextbox1.innerText;
            }else{
                spanss.style.borderColor='red';
                data_base[id].kod_anod_sn = NaN;
            }
        }
        if(combination_text.toUpperCase() != 'БЕЗ ТЕРМОМОСТА'){
            data_base[id].is_termo =true;
            var anod_sn = document.getElementById("anod_vnutr"+String(id))
            anod_sn.style.borderColor='#dedad9';
           
            const spanss =document.querySelector('#anod_vnutr'+String(id) +' .select2-container .select2-selection--single')
            const spanTextbox2 = anod_sn.querySelector('span[role="textbox"]');
            if(spanTextbox2){
                if(spanTextbox2.innerText !=''){
                    var tip_anodirovki = $('#tip_anodirovki'+String(id)).text()
                    var sposob_anodirovki = $('#sposob_anodirovki'+String(id)).text()
                    spanTextbox2.style.borderColor='#dedad9';
                    spanss.style.borderColor='#dedad9';
                    data_base[id].kod_anod_vn = spanTextbox2.innerText;
                    data_base[id].tip_anod = tip_anodirovki;
                    data_base[id].sposob_anod = sposob_anodirovki;
                }else{
                    spanTextbox2.style.borderColor='red';
                    spanss.style.borderColor='red';
                    data_base[id].kod_anod_vn = NaN;
                    data_base[id].tip_anod = NaN;
                    data_base[id].sposob_anod = NaN;
                }
            }
        }
        var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
        if(contactnost_anodirovki.val()!='0' && contactnost_anodirovki.val()!=''&& contactnost_anodirovki.val()!=null){
            
            contactnost_anodirovki.css("border-color",'#dedad9');
            data_base[id].contactnost_anod = contactnost_anodirovki.val();
        }else{

            var contactnost_anodirovki = $('#contactnost_anodirovki'+String(id));
            contactnost_anodirovki.css("border-color",'red');
            data_base[id].contactnost_anod = NaN;
        }

    }



    if(String(val) != ''){

        var sap_code_ruchnoy =$('#sap_code_ruchnoy'+id);
        var kratkiy_tekst_ruchnoy =$('#kratkiy_tekst_ruchnoy'+id);
        var online_savdo_id =$('#online_savdo_id'+id);
        var nazvaniye_ruchnoy =$('#nazvaniye_ruchnoy'+id);
        var svet_product =$('#svet_product'+id);
        var group_zakup =$('#group_zakup'+id);
        var group =$('#group'+id);
        var tip =$('#tip'+id);
        var bazoviy_edin =$('#bazoviy_edin'+id);
        var status =$('#status'+id);
        var zavod =$('#zavod'+id);
        // var zavod =$('#zavod_name'+id);

        var segment =$('#segment'+id);
        var buxgalter_tovar =$('#buxgalter_tovar'+id);
        var buxgalter_uchot =$('#buxgalter_uchot'+id);
        var alter_edin =$('#alter_edin'+id);
        var stoimost_baza =$('#stoimost_baza'+id);
        var stoimost_alter =$('#stoimost_alter'+id);
        
        
        var status_first =$('#status'+id)

        console.log(zavod.val())


        if(zavod.val() =='ZAVOD ALUMIN'){

            if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
                if(String(val) == '1'){
                    buxgalter_tovar.val('Неокрашенный алюминиевый профиль')
                }
                else if(String(val) == '2'){
                    buxgalter_tovar.val('Алюминиевый профиль')
                    
                }
                else if(String(val) == '3'){
                    
                    buxgalter_tovar.val('Алюминиевый профиль')
                }
                else if(String(val) == '4'){
                    
                    buxgalter_tovar.val('Ламинированный алюминиевый профиль')
                }
                else if(String(val) == '5'){
                    
                    buxgalter_tovar.val('Алюминиевый профиль с декоративным покрытием')
                }
                else if(String(val) == '6'){
                    buxgalter_tovar.val('')
                }
                
            }else{
                if(String(val) == '1'){
                    buxgalter_tovar.val('Неокрашенный алюминиевый профиль')
                }
                else if(String(val) == '2'){
                    buxgalter_tovar.val('Термоуплотненный окрашенный алюминиевый профиль')
                }
                else if(String(val) == '3'){
                    buxgalter_tovar.val('Термоуплотненный окрашенный алюминиевый профиль')
                    
                }
                else if(String(val) == '4'){
                    
                    buxgalter_tovar.val('Ламинированный термоуплотненный алюминиевый профиль')
                }
                else if(String(val) == '5'){
                    buxgalter_tovar.val('Алюминиевый профиль с декоративным покрытием')
                    
                }
                else if(String(val) == '6'){
                    buxgalter_tovar.val('')

                }
            }

        }else if(zavod.val() =='ZAVOD ALUMIN NAVOIY'){

            if (combination_text.toUpperCase() == 'БЕЗ ТЕРМОМОСТА'){
                if(String(val) == '1'){
                    buxgalter_tovar.val('Неокрашенный алюминиевый профиль (N)')
                }
                else if(String(val) == '2'){
                    buxgalter_tovar.val('Алюминиевый профиль (N)')
                }
                else if(String(val) == '3'){
                    buxgalter_tovar.val('Алюминиевый профиль (N)')
                }
                else if(String(val) == '4'){
                    buxgalter_tovar.val('Ламинированный алюминиевый профиль (N)')
                }
                else if(String(val) == '5'){
                    buxgalter_tovar.val('Алюминиевый профиль с декоративным покрытием (N)')
                }
                else if(String(val) == '6'){
                    buxgalter_tovar.val('')
                }

            }else{
                if(String(val) == '1'){
                    buxgalter_tovar.val('Неокрашенный алюминиевый профиль (N)')
                }
                else if(String(val) == '2'){
                    buxgalter_tovar.val('Термоуплотненный окрашенный алюминиевый профиль (N)')
                }
                else if(String(val) == '3'){
                    buxgalter_tovar.val('Термоуплотненный алюминиевый профиль (N)')
                }
                else if(String(val) == '4'){
                    buxgalter_tovar.val('Ламинированный термоуплотнённый алюминиевый профиль (N)')
                }
                else if(String(val) == '5'){
                    buxgalter_tovar.val('Алюминиевый профиль с декоративным покрытием (N)')
                }
                else if(String(val) == '6'){
                    buxgalter_tovar.val('Термоуплотненный анодированный алюминиевый профиль (N)')
                }
                
            }
        }

        

        if(status_first.val() == 'Активный'){
            if(stoimost_alter.val()!=''){
                data_base[id].stoimost_alter = stoimost_alter.val();
                
            }else{
                data_base[id].stoimost_alter = NaN;
                
            }
            if(stoimost_baza.val()!=''){
                data_base[id].stoimost_baza = stoimost_baza.val();
                
            }else{
                data_base[id].stoimost_baza = NaN;
                
            }
            if(alter_edin.val()!=''){
                data_base[id].alter_edin = alter_edin.val();
                
            }else{
                data_base[id].alter_edin = NaN;
                
            }
            if(buxgalter_uchot.val()!=''){
                data_base[id].buxgalter_uchot = buxgalter_uchot.val();
                
            }else{
                data_base[id].buxgalter_uchot = NaN;
                
            }
            if(buxgalter_tovar.val()!=''){
                data_base[id].buxgalter_tovar = buxgalter_tovar.val();
                
            }else{
                data_base[id].buxgalter_tovar = NaN;
                
            }
            if(segment.val()!=''){
                data_base[id].segment = segment.val();
                
            }else{
                data_base[id].segment = NaN;
                
            }
            if(sap_code_ruchnoy.val()!=''){
                data_base[id].sap_code = sap_code_ruchnoy.val();
                
            }else{
                data_base[id].sap_code = NaN;
                
            }
            if(kratkiy_tekst_ruchnoy.val()!=''){
                data_base[id].krat = kratkiy_tekst_ruchnoy.val();
               
            }else{
                data_base[id].krat = NaN;
                
            }
            if(online_savdo_id.val()!=''){
                online_savdo_id.css('border-color','#dedad9')
                data_base[id].online_id = online_savdo_id.val();
            }else{
                data_base[id].online_id = NaN;
                online_savdo_id.css('border-color','red')
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
            }else{
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
               
            }
            if(group_zakup.val()!=''){
                
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
                
            }
            if(group.val()!=''){
                
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                
            }
            if(tip.val()!=''){
                
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                
            }
            if(bazoviy_edin.val()!=''){
                
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                
            }
            
            if(status.val()!=''){
                
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                
            }
            if(zavod.val()!=''){
                var zavod1 =$('#zavod'+id +' option:selected').text();
                var zavod_name =$('#zavod_name'+id)
                
                zavod_name.text(zavod.val())
                data_base[id].zavod = zavod1;
                data_base[id].zavod_name = zavod.val();
            }else{
                var zavod_name =$('#zavod_name'+id)
                zavod_name.text('')
                data_base[id].zavod =NaN;
                data_base[id].zavod_name =NaN;
                
                
            }
        }else{
            if(stoimost_alter.val()!=''){
                data_base[id].stoimost_alter = stoimost_alter.val();
                
            }else{
                data_base[id].stoimost_alter = NaN;
                
            }
            if(stoimost_baza.val()!=''){
                data_base[id].stoimost_baza = stoimost_baza.val();
                
            }else{
                data_base[id].stoimost_baza = NaN;
                
            }
            if(alter_edin.val()!=''){
                data_base[id].alter_edin = alter_edin.val();
                
            }else{
                data_base[id].alter_edin = NaN;
                
            }
             if(buxgalter_uchot.val()!=''){
                data_base[id].buxgalter_uchot = buxgalter_uchot.val();
                
            }else{
                data_base[id].buxgalter_uchot = NaN;
                
            }
            if(buxgalter_tovar.val()!=''){
                data_base[id].buxgalter_tovar = buxgalter_tovar.val();
                
            }else{
                data_base[id].buxgalter_tovar = NaN;
                
            }

            if(segment.val() == 'Нет сегмента'){
                segment.css('border-color','red')
                data_base[id].segment = NaN;
                
            }else{
                segment.css('border-color','#dedad9')
                if(segment.val()==''){
                    data_base[id].segment = 'no';
                }else{
                    data_base[id].segment = segment.val();
                }
            }

            if(sap_code_ruchnoy.val()!=''){
                data_base[id].sap_code = sap_code_ruchnoy.val();
                sap_code_ruchnoy.css('border-color','#dedad9')
            }else{
                data_base[id].sap_code = NaN;
            }
            if(kratkiy_tekst_ruchnoy.val()!=''){
                data_base[id].krat = kratkiy_tekst_ruchnoy.val();
                kratkiy_tekst_ruchnoy.css('border-color','#dedad9')
            }else{
                data_base[id].krat = NaN;
            }
            if(online_savdo_id.val()!=''){
                
                data_base[id].online_id = online_savdo_id.val();
            }else{
                data_base[id].online_id = NaN;
                
            }
            if(nazvaniye_ruchnoy.val()!=''){
                nazvaniye_ruchnoy.css('border-color','#dedad9')
                data_base[id].nazvaniye_ruchnoy = nazvaniye_ruchnoy.val();
            }else{
                data_base[id].nazvaniye_ruchnoy =NaN;
                nazvaniye_ruchnoy.css('border-color','red')
            }
    
    
            if(svet_product.val()!=''){
                svet_product.css('border-color','#dedad9')
                data_base[id].svet_product = svet_product.val();
            }else{
                data_base[id].svet_product =NaN;
                svet_product.css('border-color','red')
            }
            if(group_zakup.val()!=''){
                group_zakup.css('border-color','#dedad9')
                data_base[id].group_zakup = group_zakup.val();
            }else{
                data_base[id].group_zakup =NaN;
                group_zakup.css('border-color','red')
            }
            if(group.val()!=''){
                group.css('border-color','#dedad9')
                data_base[id].group = group.val();
            }else{
                data_base[id].group =NaN;
                group.css('border-color','red')
            }
            if(tip.val()!=''){
                tip.css('border-color','#dedad9')
                data_base[id].tip = tip.val();
            }else{
                data_base[id].tip =NaN;
                tip.css('border-color','red')
            }
            if(bazoviy_edin.val()!=''){
                bazoviy_edin.css('border-color','#dedad9')
                data_base[id].bazoviy_edin = bazoviy_edin.val();
            }else{
                data_base[id].bazoviy_edin =NaN;
                bazoviy_edin.css('border-color','red')
            }
            
            if(status.val()!=''){
                status.css('border-color','#dedad9')
                data_base[id].status_online = status.val();
            }else{
                data_base[id].status_online =NaN;
                status.css('border-color','red')
            }

            
            if(zavod.val()!=''){
                zavod.css('border-color','#dedad9')
                var zavod1 =$('#zavod'+id +' option:selected').text();
                var zavod_name =$('#zavod_name'+id)

                zavod_name.text(zavod.val())
                data_base[id].zavod = zavod1;
                data_base[id].zavod_name = zavod.val();
            }else{
                var zavod_name =$('#zavod_name'+id)
                zavod_name.text('')
                data_base[id].zavod =NaN;
                data_base[id].zavod_name =NaN;

                zavod.css('border-color','red')
            }

        }
        
    }




    



    var data =data_base[id].get_kratkiy_tekst()


    if(data.accept){
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','#2de319')
        data_base[id].full=true
        data_base[id].kratkiy_tekst=data.text
    }else{
        var table_tr =$('#table_tr'+id);
        table_tr.css('background-color','white')
        data_base[id].full=false
        data_base[id].kratkiy_tekst=NaN

    }
    if(data.text !='XXXXXXXX' ){
        var art_krat = data_base[id].base_artikul + data.text
        if(zapros_count.indexOf(art_krat) === -1){
            sap_codes = get_sapcode(id,data_base[id].base_artikul,data.text,data_base[id].is_termo)
            zapros_count.push(art_krat)
        }
        data_base[id].kratkiy_tekst= data.text
        
    }
    
    kratkiy_tekst.text(data.text)

    }
}


function get_sapcode(id,artikul,kratkiy_tekst,is_termo){
    var url = '/client/get-sapcodes'
   

    $.ajax({
        type: 'GET',
        url: url,
        data: {'artikul':artikul,'kratkiy_tekst':kratkiy_tekst,'is_termo':is_termo},
    }).done(function (res) {
        if (res.status ==201){
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            
            sap_code_ruchnoy.val(res.artikul)
            kratkiy_text_ruchnoy.val(res.kratkiy_tekst)
            sap_code_ruchnoy.css('background-color','orange')
            kratkiy_text_ruchnoy.css('background-color','orange')
        }else{
            var sap_code_ruchnoy = $('#sap_code_ruchnoy'+id)
            var kratkiy_text_ruchnoy = $('#kratkiy_tekst_ruchnoy'+id)
            
            sap_code_ruchnoy.val('')
            kratkiy_text_ruchnoy.val('')
            sap_code_ruchnoy.css('background-color','white')
            kratkiy_text_ruchnoy.css('background-color','white')
            console.log('aa')
        }
        // WON'T REDIRECT
    });
}

function add_column(){
        
    text =""
    var sizeee = $('#table-artikul tr').length;
    
    text = front_piece(start = sizeee+1, end = sizeee+2)

    
    var table = $('#table-artikul')
    table.append(text)
    
    

    request_piece(start = sizeee+1, end = sizeee+2)


}






