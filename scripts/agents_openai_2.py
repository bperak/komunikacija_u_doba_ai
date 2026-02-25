from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Napiši strukturu knjige pod naslovom JEZIČNI AGENTI: RAZVOJ KOMUNIKACIJSKIH PARTNERA POMOĆU VELIKIH JEZIČNIH MODELA.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.