<h1>Automated News Scrapper</h1>
<h3>Returns in form of JSON</h3>
<h2>Requirements:</h2>
<ul>
  <li>Python 3.7</li>
  <li>Selenium (Chromium)</li>
</ul>
<h2>Application in web page:</h2>
<h3>https://news.gabrielkheisa.xyz/</h3>
<h2>Example:</h2>
<ul>
    <li>https://api.gabrielkheisa.xyz/news/antaranews/</li>
    <pre>
    {
  "server_update": "08-11-2022 12:50:44",
   "news": [
    {
      "judul": "IKN development with Forest City concept to mitigate climate change",
       "berita": "",
       "URL": "https://en.antaranews.com/news/259041/ikn-development-with-forest-city-concept-to-mitigate-climate-change",
       "gambar": null,
       "tgl": " 19 minutes ago"
    },
     {
      "judul": "Gov't should conduct COVID-19 test again amid XBB spread:  Asmoro",
       "berita": "",
       "URL": "https://en.antaranews.com/news/259037/govt-should-conduct-covid-19-test-again-amid-xbb-spread-asmoro",
       "gambar": null,
       "tgl": " 51 minutes ago"
    },
     {
      "judul": "Indonesian military builds six church bell towers in Papua",
       "berita": "",
       "URL": "https://en.antaranews.com/news/208661/indonesian-military-builds-six-church-bell-towers-in-papua",
       "gambar": null,
       "tgl": " 9th January 2022"
    },
     {
      "judul": "Ancol Dreamland, Asuransi Astra, Hilo, Janji Jiwa Jiwa Toast are among the winners of the 2022-2023 Brand of the Year Awards.",
       "berita": "",
       "URL": "https://en.antaranews.com/news/259029/ancol-dreamland-asuransi-astra-hilo-janji-jiwa-jiwa-toast-are-among-the-winners-of-the-2022-2023-brand-of-the-year-awards",
       "gambar": null,
       "tgl": " 5 hours ago"
    }
  ]
}
    </pre>
    <li>https://api.gabrielkheisa.xyz/news/coindesk/</li>
    <pre>
    {
  "server_update": "08-11-2022 12:25:51",
   "news": [
    {
      "judul": "Bitcoin, Ether Slide as Protective Puts Draw Demand Amid Sell-Off in FTX's Token",
       "berita": "Options market tied to bitcoin and ether shows renewed bias for puts, perhaps a sign of investor fears that the FTX-Alameda drama may bring another market-wide crash.",
       "URL": "https://www.coindesk.com/markets/2022/11/08/bitcoin-ether-slide-as-protective-puts-draw-demand-amid-sell-off-in-ftx-token/",
       "gambar": "",
       "tgl": "Nov 8, 2022"
    },
     {
      "judul": "FTX Token Plummets as Market Fears Possible Alameda Contagion",
       "berita": "FTT was down nearly 12% in the last hour and over 20% during the last 24 hours.",
       "URL": "https://www.coindesk.com/markets/2022/11/08/ftt-plummets-as-market-fears-possible-alameda-contagion/",
       "gambar": "",
       "tgl": "Nov 8, 2022"
    },
     {
      "judul": "First Mover Asia: A Good Week for Exchange Tokens, Except FTT; Solana Continues Falling",
       "berita": "During the past week, a number of exchange tokens have outperformed bitcoin, including OKX and CRO.  FTT is not among them.",
       "URL": "https://www.coindesk.com/markets/2022/11/08/first-mover-asia-a-good-week-for-exchange-tokens-except-ftt-solana-continues-falling/",
       "gambar": "",
       "tgl": "Nov 8, 2022"
    },
     {
      "judul": "Market Wrap: Solana Plunge Highlights Major Cryptos\u2019 Day in the Red",
       "berita": "The native token of the Solana protocol recently fell over 6%; bitcoin and ether dropped more modestly as investors await the midterm elections and latest inflation data. Market Wrap is CoinDesk\u2019s daily newsletter diving into what happened in today's crypto markets.",
       "URL": "https://www.coindesk.com/markets/2022/11/07/market-wrap-solana-plunge-highlights-major-cryptos-day-in-the-red/",
       "gambar": "",
       "tgl": "Nov 8, 2022"
    }
  ]
}
    </pre>
    <li>https://api.gabrielkheisa.xyz/news/gsmarena/</li>
    <pre>
    {
  "server_update": "08-11-2022 12:42:33",
   "news": [
    {
      "judul": "Google releases stable November Android 13 update, new QPR1 Beta 3.1 too",
       "berita": "As it was just the first Monday of the month, Google released the latest monthly Android update for its still-supported Pixels mere hours ago. The November 2022 update is the last minor one before the bigger December release - which has been in open...",
       "URL": "https://www.gsmarena.com/google_releases_stable_november_android_13_update_new_qpr1_beta_31_too-news-56434.php",
       "gambar": "https://fdn.gsmarena.com/imgroot/news/22/11/google-november-update/-344x215/gsmarena_000.jpg",
       "tgl": "08 November 2022"
    },
     {
      "judul": "Google reveals its upcoming Black Friday deals for Pixel 7, Pixel 7 Pro, and Pixel 6a",
       "berita": "Google is very excited about Black Friday this year, and as such it's letting us know in advance what the deals will be. Over at its online store, the company is now prominently displaying a countdown clock to the start of the deals. At the time of...",
       "URL": "https://www.gsmarena.com/google_reveals_its_upcoming_black_friday_deals_for_pixel_7_pixel_7_pro_and_pixel_6a-news-56433.php",
       "gambar": "https://fdn.gsmarena.com/imgroot/news/22/11/google-black-friday-deals/-344x215/gsmarena_000.jpg",
       "tgl": "08 November 2022"
    },
     {
      "judul": "Samsung sets new speed record over 5G - 1.75Gbps at 10km distance",
       "berita": "Samsung Electronics announced that it reached record-breaking transfer speeds over a 5G mmWave network. The tests were carried out in partnership with NBN Co. a company that is part of an AUD 750 million investment plan in Australia. NBN is using...",
       "URL": "https://www.gsmarena.com/samsung_reaches_insane_download_speeds_over_5g_10km_away_from_source-news-56432.php",
       "gambar": "https://fdn.gsmarena.com/imgroot/news/20/10/samsung-q3-report/-344x215/gsmarena_001.jpg",
       "tgl": "07 November 2022"
    },
     {
      "judul": "Xiaomi Redmi K60 confirmed to support 67W fast charging",
       "berita": "Xiaomi's upcoming Redmi K60 flagship series is set to debut in the coming weeks, although there's still no official date set. The intensity of recent leaks suggests that's fast approaching, and so do the certification documents that are now flying...",
       "URL": "https://www.gsmarena.com/xiaomi_redmi_k60_confirmed_to_support_67w_fast_charging-news-56431.php",
       "gambar": "https://fdn.gsmarena.com/imgroot/news/22/03/xiaomi-redmi-k50-colors/-344x215/gsmarena_001.jpg",
       "tgl": "07 November 2022"
    }
  ]
}
    </pre>
    <li>https://api.gabrielkheisa.xyz/news/theverge/</li>
    <pre>
    {
  "server_update": "08-11-2022 12:54:01",
   "news": [
    {
      "judul": "Elon Musk has discussed putting all of Twitter behind a paywall",
       "berita": "",
       "URL": "https://www.theverge.com/2022/11/7/23446262/elon-musk-twitter-paywall-possible",
       "gambar": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
       "tgl": "8:52 AM GMT+7"
    },
     {
      "judul": "AMC is working with Zoom to turn some theaters into giant meeting rooms",
       "berita": "",
       "URL": "https://www.theverge.com/2022/11/7/23446136/amc-zoom-rooms-theaters-meetings",
       "gambar": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
       "tgl": "8:38 AM GMT+7"
    },
     {
      "judul": "How am I supposed to mark myself as parody if I can\u2019t change my screen name, Elon?",
       "berita": "",
       "URL": "https://www.theverge.com/2022/11/7/23446171/screen-name-twitter-musk-parody-whoops",
       "gambar": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
       "tgl": "8:32 AM GMT+7"
    },
     {
      "judul": "T-Mobile may be looking to spend big on fiber home internet",
       "berita": "",
       "URL": "https://www.theverge.com/2022/11/7/23445777/t-mobile-home-internet-fiber-5g-partnership-search",
       "gambar": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
       "tgl": "6:09 AM GMT+7"
    }
  ]
}
    </pre>
    <li>https://api.gabrielkheisa.xyz/news/steam/</li>
    <pre>
    {
  "server_update": "08-11-2022 23:07:24",
   "games": [
    {
      "nama": "New World",
       "harga_asli": "Rp 249 999",
       "harga_diskon": "Rp 124 999",
       "persen": "-50%",
       "url": "https://store.steampowered.com/app/1063730?snr=1_2300_4__salesmartpopularpurchased"
    },
     {
      "nama": "Warhammer: Vermintide 2",
       "harga_asli": "Rp 189 999",
       "harga_diskon": "Rp 37 999",
       "persen": "-80%",
       "url": "https://store.steampowered.com/app/552500?snr=1_2300_4__salesmartpopularpurchased"
    },
     {
      "nama": "Deep Rock Galactic",
       "harga_asli": "Rp 139 999",
       "harga_diskon": "Rp 46 199",
       "persen": "-67%",
       "url": "https://store.steampowered.com/app/548430?snr=1_2300_4__salesmartpopularpurchased"
    },
     {
      "nama": "Dead Cells",
       "harga_asli": "Rp 149 999",
       "harga_diskon": "Rp 89 999",
       "persen": "-40%",
       "url": "https://store.steampowered.com/app/588650?snr=1_2300_4__salesmartpopularpurchased"
    },
     {
      "nama": "Slay the Spire",
       "harga_asli": "Rp 119 999",
       "harga_diskon": "Rp 40 799",
       "persen": "-66%",
       "url": "https://store.steampowered.com/app/646570?snr=1_2300_4__salesmartpopularpurchased"
    }
  ]
}
    </pre>
    
</ul>