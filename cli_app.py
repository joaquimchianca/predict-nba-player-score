import argparse
import sys
from model import setup, trainer
from sklearn.metrics import accuracy_score
import os


def main():
    parser = argparse.ArgumentParser("app")
    parser.add_argument('--name', '-n', type=str, help="Nome do jogador")
    parser.add_argument('--points', '-p', type=float, help="Limite de pontos")
    parser.add_argument('--list-players', action='store_true', help='Listar todos os jogadores')

    
    args = parser.parse_args()
    data = setup.load_data('./database_csv.csv')

    if args.list_players:
        if os.path.exists('players_list.txt'):
            os.remove('players_list.txt')
        setup.list_players(data)
        sys.exit(0)
    
    if not args.name or not args.points:
        print("Erro: O nome do jogador e o limite de pontos são obrigatórios.")
        parser.print_help()
        sys.exit(1)

    if args.points <= 0:
        print("Erro: O limite de pontos deve ser positivo")
        sys.exit(1)
    

    print(f"Nome do jogador: {args.name}")
    print(f"Limite de pontos para previsão: {args.points}")

    X_train, y_train, X_test, y_test, pts_last_game = setup.prepare_data(data, args.name, args.points)

    # chamada para treinamento do algoritmo
    gbm = trainer.train_gbm(X_train, y_train)

    y_pred = gbm.predict(X_test)[0]

    result = "acima" if y_pred else "abaixo"
    print(f"\n{args.name} vai marcar {result} de {args.points} pontos na próxima partida.")
    print(f"No último jogo, {args.name} marcou {pts_last_game} pontos.")

    # accuracy_pct = accuracy_score([y_test.values[0]], [y_pred]) * 100
    # print(f"\nAcurácia do modelo: {accuracy_pct:.2f}%")

if __name__ == '__main__':
    main()
    