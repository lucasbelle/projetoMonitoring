BUY_PAGE_HTML = """
<html>
<head>
    <title>Comprar</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .card {
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            text-align: center;
            width: 320px;
        }

        h1 {
            font-size: 22px;
            margin-bottom: 15px;
            color: #333;
        }

        p {
            color: #555;
            margin-bottom: 25px;
        }

        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 12px 22px;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
            transition: background 0.2s ease;
        }

        button:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Finalizar Compra</h1>
        <p>Clique no botão abaixo para concluir sua compra.</p>

        <form action="/checkout" method="get">
            <button type="submit">Finalizar</button>
        </form>
    </div>
</body>
</html>
"""
