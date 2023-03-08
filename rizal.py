import os
from dotenv import load_dotenv
from eospy.cleos import Cleos
from eospy.keys import EOSKey

load_dotenv()

url = 'http://108.175.1.159:8888'
ce = Cleos(url=url)

private_key = os.getenv("PRIV_KEYS")
actor = os.getenv("INERY_NAME")

account = "ashev22"
key = EOSKey(private_key)
data = {"id": 1, "user": account, "data": "INERY TESTNET TASK4"}

async def create(data):
    try:
        resp = ce.push_transaction(
            {
                "actions": [
                    {
                        "account": account,
                        "name": "create",
                        "authorization": [
                            {
                                "actor": actor,
                                "permission": "active",
                            }
                        ],
                        "data": data,
                    }
                ]
            },
            key,
            broadcast=True,
            sign=True,
        )

        print("=======================================================================")
        print("=================== CREATE transaction information ====================")
        print("=======================================================================")
        print(resp, "\n")
        print("Response from contract :", resp["processed"]["action_traces"][0]["console"])
        print("\n")
    except Exception as e:
        print(str(e))

async def destroy(id):
    try:
        resp = ce.push_transaction(
            {
                "actions": [
                    {
                        "account": account,
                        "name": "destroy",
                        "authorization": [
                            {
                                "actor": actor,
                                "permission": "active",
                            }
                        ],
                        "data": {
                            "id": id,
                        },
                    }
                ]
            },
            key,
            broadcast=True,
            sign=True,
        )

        print("=======================================================================")
        print("================== DESTROY transaction information ====================")
        print("=======================================================================")
        print(resp, "\n")
        print("Response from contract :", resp["processed"]["action_traces"][0]["console"])
        print("\n")
    except Exception as e:
        print(str(e))


async def main(id, user, data):
    await create(data)
    await destroy(id)


if __name__ == "__main__":
    data = {"id": 1, "user": account, "data": "INERY TESTNET TASK4"}
    main(data["id"], data["user"], data["data"])
