#-*-coding:utf-8-*-
#===============================================================================
# 	Copyright 2012 Vadim Suharnikov <v.suharnikov@gmail.com>
#
#	This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from __future__ import division
from pylab import *
from random import gauss

class galaxy_generator(object):
	def speral_galaxy(self, nStars=50000, arms=2, mAng=1, dAng=1, mDist=1, dDist=1.2, kAng=1, kDist=1, kDist1=1000000000, kDist2=.247):
		x = []
		y = []
		for _ in xrange(nStars):
			ang = (gauss(mAng, dAng) + arms ** -1) * np.pi * kAng
			dist = (gauss(mDist, dDist + 0.2) * kDist1 / arms) + np.exp(ang * kDist2) * kDist1
			ang += np.pi * 2 / arms * randint(arms)
			x.append(sin(ang) * dist)
			y.append(cos(ang) * dist)
		return np.array(x), np.array(y)
