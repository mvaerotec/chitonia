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

In the game, you will need to make the players interact between them and solve situations that may arise.
These situations may arise randomly at the end of every turn, changing the state of the players, so watch out for the prompts or check the states regularly.

Points
^^^^^^

Players have a set of points that can be consulted by requesting player's states. These points decrease in each turn, and the players can earn points back by interacting between each other.

If any player's points fall below a certain threshold, you will be warned. If points fall to 0, game will end, so watch out carefully for information!

.. note:: Now you have everything you need to start playing. From here the rest of the documentation can make spoilers, so it is better to just play and discover the interactions by yourself rather than reading them here!

End of turn
^^^^^^^^^^^

There are four different end-of-turn situations (eots) that can arise at the end of every turn:

- Pomtito starts barking someone and you need to calm him down. To solve it, just play with him, take him for a walk (both Pomtito actions) or love him (any other player).
- Gatete starts being hungry and you need to feed him. You must use Chito or Chita to do so.
- Chito gets mimochi and needs mimich. Chita, Pomtito or Gatete must love him to remove this state.
- Chito lia something and needs chita to fix it. Chita needs to go and fix the liada.

Player unavailability
^^^^^^^^^^^^^^^^^^^^^

Also, players may be unavailable to perform any action, and you may need to select them again. Depending on the player, selecting them a second time can make them available, but that is not for granted.
A player's unavailability does not count for new eots or decreasing points.

Unavailabilities are the following:

- Chita during her siesta.
- Mamichita during her siesta and her daily conversation with Cayo.
- Pomtito if he is in state vaguete and he does not want to act.
- Gatete is a gato and sometimes he is just ignoring you.
