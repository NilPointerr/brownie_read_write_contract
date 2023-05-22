from brownie import accounts, calculator
import os
from dotenv import load_dotenv

load_dotenv()


def deploy_contract():
    # account = accounts[0]
    account = accounts.load("nilesh-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    print("env", account)
    # print(account)

    cal_deploy = calculator.deploy({"from": account}, publish_source=True)
    print(cal_deploy)

    multiply_call = cal_deploy.calculate(25, 30, "*", {"from": account})
    print(multiply_call)
    output = cal_deploy.viewAns()
    print(output)


def main():
    deploy_contract()
