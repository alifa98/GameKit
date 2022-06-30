{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "dc6b6eb2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "Men = int(input())\n",
    "Women = Men = int(input())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "f3b5dc77",
   "metadata": {},
   "outputs": [],
   "source": [
    "# if women wi prefer man mj function return true\n",
    "\n",
    "# this woman = w\n",
    "# current engamement = m1\n",
    "# new request = m\n",
    "# if w prefers m over m1\n",
    "def wPrefer(prefer, w, m, m1):\n",
    "    \n",
    "    for i in range(Men):\n",
    "        \n",
    "        \n",
    "        # preference of w:  ... m1, ..., m, ...\n",
    "        if (prefer[w][i] == m1):\n",
    "            return True\n",
    "        # preference of w:  ... m, ..., m1, ...\n",
    "        if (prefer[w][i] == m):\n",
    "            return False\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "558cdc7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def stableMarriage(prefer):\n",
    "    \n",
    "    # allocated man to woman[i] store here\n",
    "    wPartner = [-1 for i in range(Women)]\n",
    "    \n",
    "    # single man notificed by false value\n",
    "    mFree = [False for i in range(Men)]\n",
    "    \n",
    "    # we work on men-proposing algorithm\n",
    "    # so start with man-count\n",
    "    freeCount = Men\n",
    "    \n",
    "    while (freeCount > 0):\n",
    "        \n",
    "        # pick up first false man\n",
    "        # this = first single man\n",
    "        this = 0\n",
    "        while (this < Men):\n",
    "            if (mFree[this] == False):\n",
    "                break\n",
    "            this += 1\n",
    "        \n",
    "        \n",
    "        # request each woman of his preference\n",
    "        request = 0\n",
    "        while request < Women and mFree[this] == False:\n",
    "            w = prefer[this][request]\n",
    "        \n",
    "            # if requested woman is free, so you can engage\n",
    "            if (wPartner[w - Men] == -1):\n",
    "                # matching better than unmatching\n",
    "                wPartner[w - Men] = this\n",
    "                mFree[this] = True\n",
    "                freeCount -= 1\n",
    "            # if requested woman engage, it's depend:\n",
    "            else:\n",
    "                \n",
    "                # find partner of w\n",
    "                m1 = wPartner[w - Men]\n",
    "                \n",
    "                # if w prefer 'this' over her current engagement m1:\n",
    "                # break up with m1 :(\n",
    "                # engage with this \n",
    "                if (wPrefer(prefer, w, this, m1) == False):\n",
    "                    wPartner[w - Men] = this\n",
    "                    mFree[this] = True\n",
    "                    mFree[m1] = False\n",
    "                    \n",
    "                # else: woman not prefere this to her current engaement\n",
    "                # nothing happen\n",
    "                else:\n",
    "                    pass\n",
    "                \n",
    "\n",
    "                    \n",
    "            request += 1\n",
    "             \n",
    "    return wPartner"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "id": "e08fe95b",
   "metadata": {},
   "outputs": [],
   "source": [
    "prefer = [[7, 5, 6, 4], [5, 4, 6, 7],\n",
    "          [4, 5, 6, 7], [4, 5, 6, 7],\n",
    "          [0, 1, 2, 3], [0, 1, 2, 3],\n",
    "          [0, 1, 2, 3], [0, 1, 2, 3]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "id": "852b2460",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "result = stableMarriage(prefer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "53b30195",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 1, 3, 0]"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
