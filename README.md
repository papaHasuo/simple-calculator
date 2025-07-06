# Simple Calculator

このプロジェクトは、MCP（Model Context Protocol）の動作検証・学習を目的とした、Python製のシンプルな電卓アプリケーションです。

## プロジェクト概要

- MCPの基本的な使い方やAPI連携の仕組みを試すためのサンプルです。
- 四則演算（足し算、引き算、掛け算、割り算）をMCP経由で実行できます。
- MCPサーバやクライアントの開発・テストの入門用として利用できます。

## 構成

- `main.py`: 電卓のメインプログラム。MCPのエンドポイントを呼び出して計算を行います。
- `pyproject.toml`: プロジェクトの依存関係と設定。
- `uv.lock`: 依存関係のロックファイル。
- `README.md`: このファイル。

## 使い方(VSCodeのGithub Copilotで使うための方法)

1. vscodeディレクトリを作成してください。
2. setting.jsonに、以下のようにMCP用の設定を記述してください。
```json
{
    "mcp": {
        "servers": {
            "simple-calculator": {
                "command": "uv",
                "args": [
                    "--directory",
                    "{プロジェクトファイルのディレクトリ（絶対パス）}",
                    "run",
                    "main.py",
                ],
            },
        }
    }
}
```
3. VSCode上でMCP一覧を開き、この`simple-calculator`があることを確認して実行してください。
`Ctrl+Shift+P`でMCPと検索すれば出てきます。
