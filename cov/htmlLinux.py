def writeLog(file, text):
    with open(file, 'a+') as f:
        f.write(f'{text}\n')


def htmlMaker():
    partOne = '''
    <html lang = "pl">
    <head>
    <meta name="COV2020" content="Covid Statistic">
    <meta name="description" content="Filip Nowainski Project Site">
    <meta name="keywords" content="filipnowainski.pl, filip, nowainski, Filip, Nowainski">
    <meta name="robots" content="index, follow">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="language" content="pl">
    <style>
    .divTex {
    text-align: center;
    }


    div.gallery {
      border: 1px solid #ccc;
    }

    div.gallery:hover {
      border: 1px solid #777;
    }



    div.gallery {
      border: 1px solid #ccc;
    }

    div.gallery:hover {
      border: 1px solid #777;
    }


    div.gallery img {
      width: 100%;
      height: 100px;
    }





    div.desc {
      padding: 15px;
      text-align: center;
    }


    * {
      box-sizing: border-box;
    }


    * {
      box-sizing: border-box;
    }

    .responsive {
      padding: 0 6px;
      float: left;
      width: 24.99999%;
    }

    @media only screen and (max-width: 700px) {
      .responsive {
        width: 49.99999%;
        margin: 6px 0;
      }
    }
    @media only screen and (max-width: 500px) {
      .responsive {
        width: 100%;
      }
    }

    .clearfix:after {
      content: "";
      display: table;
      clear: both;
    }
    </style>
    </head>
    <body>

    <div class="divTex">
    <h2>Coronavirus Disease 2019 statistic</h2>
    <h5><a href="../main.html"> HOME</a></h5>
    </div>
        '''

    partThree = '''
        </body>
        </html>
    '''
    partTwo = ''
    import os

    pngList = []
    for root, _, files in os.walk('plots'):
        for name in files:
            pngList.append(os.path.join(root, name))
    for P in pngList:
        partTwo = partTwo + f'''
                        <div class="responsive">
                            <div class="gallery">
                                <a target="_blank" href="plots/{os.path.basename(P)}">
                                    <img src="flags/{os.path.basename(P)}" alt="{os.path.basename(P).replace(".png", "")}" width="600" height="400">
                                </a>
                                <div class="desc">{os.path.basename(P).replace(".png", "")[0:20]}</div>
                            </div>
                        </div>
                '''

    with open('index.html', 'w+') as f:
        f.write(partOne + partTwo + partThree)

    return True






