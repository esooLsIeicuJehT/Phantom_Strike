"""
BloodStrike Python SDK - Core Module
Interfaces with BloodStrike's embedded CPython engine
"""

from .sdk import BloodStrikeSDK, Vector3, MathUtils
from .entity import Entity, EntityManager

__all__ = ['BloodStrikeSDK', 'Entity', 'EntityManager', 'Vector3', 'MathUtils']