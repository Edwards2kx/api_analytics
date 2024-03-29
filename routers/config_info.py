from fastapi import APIRouter

router = APIRouter()
thirPartyApps = [
    "br.com.gerenciadorfinanceiro.controller",
    "co.aflore.my_aflore_client",
    "co.com.bancofalabella.mobile.omc",
    "co.com.bancolombia.canalesmoviles.apppyme",
    "co.com.bbva.mb",
    "co.com.tcs.bancolombia.bancaalamano",
    "com.airtm.android",
    "com.akbank.android.apps.akbank_direkt",
    "com.bancodebogota.bancamovil",
    "com.bbva.BBVAMovilCO.iphoneos",
    "com.bbva.bbvawalletco",
    "com.binance.dev",
    "com.comppra.powwi",
    "com.czzhao.binance",
    "com.davivienda.appdavivienda",
    "com.davivienda.daviplataapp",
    "com.davivienda.daviviendaapp",
    "com.devnied.currency.free",
    "com.dinero.profin.prestamo.credito.credit.credibus.loan.efectivo.cash",
    "com.elefantetech.monetapp",
    "com.etoro.openbook",
    "com.finansbank.mobile.cepsube",
    "com.firstrade.android",
    "com.grupoavalav1.bancamovil",
    "com.ibm.fna.movil",
    "com.idinero.cash.prestamo.credit",
    "com.investing.app",
    "com.ionicframework.myapp686494",
    "com.mercadopago.wallet",
    "com.nequi.MobileApp",
    "com.nu.production",
    "com.pagalo.mobile",
    "com.paypal.android.p2pmobile",
    "com.paypal.ios",
    "com.payvalida.wallet",
    "com.processa.mobility.issuer.bancamia",
    "com.ProteccionApp",
    "com.tdameritrade.mobile3",
    "com.todo1.davivienda.mobileapp",
    "com.todo1.mobile",
    "com.transferwise.ios",
    "com.uphold.wallet",
    "com.visa.lac.benefits",
    "com.ykb.android",
    "es.payflow.app",
    "eu.netinfo.colpatria.system",
    "insights.investments.app",
    "money.expense.budget.wallet.manager.track.finance.tracker",
    "org.dayup.stocks"
]

@router.get("/")
async def root():
    return {"android_apps_package_name": thirPartyApps}
