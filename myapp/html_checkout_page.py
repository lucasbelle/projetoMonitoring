CHECKOUT_SUCCESS_HTML = """
<html>
<head>
    <title>Compra Finalizada</title>
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
            width: 350px;
        }

        h1 {
            font-size: 24px;
            margin-bottom: 15px;
            color: #333;
        }

        p {
            color: #555;
            margin-bottom: 25px;
        }

        .success-icon {
            font-size: 48px;
            color: #4CAF50;
            margin-bottom: 15px;
        }

        a {
            display: inline-block;
            margin-top: 10px;
            padding: 10px 18px;
            background: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: background 0.2s ease;
        }

        a:hover {
            background: #45a049;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="success-icon">✓</div>
        <h1>Compra Finalizada</h1>
        <p>Seu checkout foi concluído com sucesso.</p>

        <a href="/buy">Voltar à Loja</a>
    </div>
</body>
</html>
"""
