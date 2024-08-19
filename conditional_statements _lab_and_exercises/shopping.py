budget = float(input())
graph_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

PRICE_PER_GRAPH_CARD = 250
PRICE_PER_PROCESSOR = graph_cards_count * PRICE_PER_GRAPH_CARD * 0.35
PRICE_PER_RAM_MEMORY = graph_cards_count * PRICE_PER_GRAPH_CARD * 0.10

total = graph_cards_count * PRICE_PER_GRAPH_CARD \
        + processors_count * PRICE_PER_PROCESSOR \
        + ram_memory_count * PRICE_PER_RAM_MEMORY

if graph_cards_count > processors_count:
    total = total - total * 0.15

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(budget - total):.2f} leva more!")
