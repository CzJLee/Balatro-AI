# Balatro AI

A personal project to attempt to train a reinforcement learning model to play [Balatro](https://www.playbalatro.com).

## Dependencies

Running this model has a few dependencies:
- [Balatro v1.0.1m-FULL](https://store.steampowered.com/app/2379780/Balatro/)
- [Lovely Injector](https://github.com/ethangreen-dev/lovely-injector)
	- Allows Lua code injection for Love2D games.
- [Steamodded](https://github.com/Steamopollys/Steamodded)
	- Mod loader and injector for Balatro.
- [Balatrobot](https://github.com/besteon/balatrobot)
	- Opens a port to run bots for Balatro

## Reinforcement Learning

The framework that I was suggested to use is [[Stable Baselines3]].

## Launch Balatro with mods

```shell
sh ~/Library/Application\ Support/Steam/steamapps/common/Balatro/run_lovely.sh
```

### List of actions

This is the list of all actions available to the bot.

- `select_blind`
- `skip_blind`
- `play_hand`
- `discard_hand`
- `end_shop`
- `reroll_shop`
- `buy_card`
- `buy_voucher`
- `buy_booster`
- `select_booster_card`
- `skip_booster_pack`
- `sell_joker`
- `use_consumable`
- `sell_consumable`
- `rearrange_jokers`
- `rearrange_consumables`
- `rearrange_hand`
- `pass`
- `start_run`
- `send_gamestate`