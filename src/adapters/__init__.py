"""Source-specific readers for external benchmarks.

These readers audit native source schemas.  They do not share a prompt compiler
and intentionally do not emit final benchmark items until each transformation
contract has been reviewed and frozen.
"""
