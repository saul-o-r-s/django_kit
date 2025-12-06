from django.http import HttpResponse

def hola_mundo(request):
    """
    Kit de Documentación sobre las terminales de Windows
    """

    html_content = """
    <html>
    <head>
        <title>Página del Kit sobre las terminales de Windows</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                background-color: #000000; /* Fondo negro */
                font-family: Arial, sans-serif;
                color: white; /* Texto blanco */
            }

            /* Barra superior */
            .navbar {
                width: 100%;
                background-color: #ffffff; /* Blanca */
                padding: 15px;
                text-align: center;
                box-shadow: 0px 2px 10px rgba(255,255,255,0.2);
                position: fixed;
                top: 0;
                left: 0;
            }

            .navbar h1 {
                margin: 0;
                color: black; /* Texto negro dentro de barra blanca */
                font-size: 22px;
                font-weight: bold;
            }

            /* Contenido */
            .content {
                margin-top: 100px; /* Se baja para no tapar la barra */
                text-align: center;
            }

            /* Botones blancos */
            .btn {
                background-color: white;
                color: black;
                padding: 12px 20px;
                text-decoration: none;
                font-weight: bold;
                border-radius: 8px;
                border: 2px solid white;
                display: inline-block;
                margin: 10px;
            }

            .btn:hover {
                background-color: black;
                color: white;
                border: 2px solid white;
            }

            .section-title {
                margin-top: 40px;
                font-size: 24px;
                text-decoration: underline;
            }

        </style>
    </head>
    <body>

        <!-- Barra superior -->
        <div class="navbar">
            <h1>Página del Kit sobre las terminales de Windows</h1>
        </div>

        <div class="content">

            <h2>Bienvenido al Kit de Documentación</h2>
            <p>Recursos y materiales para aprender sobre terminales en Windows.</p>

            <div>
                <a class="btn" href="#">Documento 1</a>
                <a class="btn" href="#">Documento 2</a>
                <a class="btn" href="#">Documento 3</a>
            </div>

            <h3 class="section-title">Materiales adicionales</h3>

            <!-- =============================== -->
            <!-- AQUI PUEDES AGREGAR OTROS ARCHIVOS -->
            <!-- Ejemplo: subir infografía -->
            <!-- <a class="btn" href="/media/infografia.pdf">Ver Infografía</a> -->

            <!-- Ejemplo: subir presentación -->
            <!-- <a class="btn" href="/media/presentacion.pptx">Ver Presentación</a> -->

            <!-- Ejemplo: subir guía técnica -->
            <!-- <a class="btn" href="/media/guia.pdf">Guía Técnica</a> -->

            <!-- Ejemplo: agregar video -->
            <!-- <video width="400" controls>
                    <source src="/media/video.mp4" type="video/mp4">
               </video> -->
            <!-- =============================== -->

        </div>

    </body>
    </html>
    """

    return HttpResponse(html_content)
