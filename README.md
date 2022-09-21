# BestBet

## Set up local environment(backend)

- To set up local environment we will be using pipenv. So if you do not have pipenv installed install it using this command:
```bash
pip install --user pipenv
```

- Install required packages with:
```bash
cd api && pipenv install
```
- Activate your pipenv environment:
```bash
pipenv shell
```

- Run the server with:
```bash
uvicorn app:app --reload 
```