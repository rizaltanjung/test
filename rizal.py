from  ineryjs.dist import Api, JsonRpc, RpcError, JsSignatureProvider
import os
from dotenv import load_dotenv
load_dotenv()

url = "http://108.175.1.159:8888"

json_rpc = JsonRpc(url)
private_key = os.getenv("PRIV_KEYS")
actor = os.getenv("INERY_NAME")

account = "ashev22"
signature = JsSignatureProvider([private_key])

api = Api(
    rpc=json_rpc,
    signature_provider=signature
)

async def create(id, user, data):
    try:
        tx = await api.transact({
            "actions": [
                {
                    "account": account,
                    "name": "create",
                    "authorization": [
                        {
                            "actor": actor,
                            "permission": "active"
                        }
                    ],
                    "data": {
                        "id": id,
                        "user": user,
                        "data": data
                    }
                }
            ]
        }, {
            "broadcast": True,
            "sign": True
        })

        print("=======================================================================")
        print("=================== CREATE transaction information ====================")
        print("=======================================================================")
        print(tx, "\n")
        print("Response from contract :", tx["processed"]["action_traces"][0]["console"])
        print("\n")
    except RpcError as error:
        print(error)

async def destroy(id):
    try:
        tx = await api.transact({
            "actions": [
                {
                    "account": account,
                    "name": "destroy",
                    "authorization": [
                        {
                            "actor": actor,
                            "permission": "active"
                        }
                    ],
                    "data": {
                        "id": id
                    }
                }
            ]
        }, {
            "broadcast": True,
            "sign": True
        })

        print("=======================================================================")
        print("================== DESTROY transaction information ====================")
        print("=======================================================================")
        print(tx, "\n")
        print("Response from contract :", tx["processed"]["action_traces"][0]["console"])
        print("\n")
    except RpcError as error:
        print(error)

async def main(id, user, data):
    await create(id, user, data)
    await destroy(id)

if __name__ == '__main__':
    main(1, account, "INERY TESTNET TASK4")
