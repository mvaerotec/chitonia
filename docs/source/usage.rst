Usage
=====

.. _installation:

Installation
------------

There is no installation for Chitonia, you must just clone its repository using
the following command::

    $ git clone https://github.com/mvaerotec/chitonia.git

Then you can execute the game executing the `main.py` file::

    $ python3 main.py

Players
-------

The game contains 5 players:

.. autoclass:: src.players.chita.Chita
.. autoclass:: src.players.chito.Chito
.. autoclass:: src.players.gatete.Gatete
.. autoclass:: src.players.pomtito.Pomtito
.. autoclass:: src.players.mamichita.Mamichita

How to play
-----------

.. note:: It is better to just play and discover the interactions by yourself rather than reading them here!

In the game, you will need to make the players interact between them and solve situations that may arise.
These situations may arise randomly at the end of every turn, changing the state of the players, so watch out for the prompts or check the states regularly.

There are four different situations that can arise at the end of every turn:

- Pomtito starts barking someone and you need to calm him down. To solve it, just play with him, take him for a walk (both Pomtito actions) or love him (any other player).
- Gatete starts being hungry and you need to feed him. You must use Chito or Chita to do so.
- Chito gets mimochi and needs mimich. Chita, Pomtito or Gatete must love him to remove this state.
- Chito lia something and needs chita to fix it. Chita needs to go and fix the liada.

Also, players may be unavailable. Unavailabilities are the following:

- Chita during her siesta.
- Mamichita during her siesta and her daily conversation with Cayo.
- Pomtito if he is in state vaguete and he does not want to act.
- Gatete is a gato and sometimes he is just ignoring you.
