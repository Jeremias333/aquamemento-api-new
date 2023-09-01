# aquamemento-api-new

## Execução
$ source .venv/bin/activate

$ uvicorn server:app --host 127.0.0.1 --port 8000 --reload

## Tests
> Testes unitários
$ pytest -v

> Testes de cobertura
$ pytest --cov test/

## Todo
- [ ] Implementar ORM
- [ ] Implementar testes
- [ ] Implementar controllers
- [x] Implementar models
- [ ] Implementar rotas
- [ ] Inicializar dados iniciais 

## Tecnologias utilizadas

- [Python 3.8](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Peewee](http://docs.peewee-orm.com/en/latest/)
- [Pytest](https://docs.pytest.org/en/stable/)

## Fluxo

> Criar um novo usuário

