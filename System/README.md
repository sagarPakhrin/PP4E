# String Method basics
`>>> mystr = 'xxxSPAMxxx'`
`>>> mystr.find('SPAM')`
`3`

`>>> mystr = 'xxxaaxxa'`
`>>> mystr.replace('aa','SPAM')`
`xxSPAMxxSPAM`


`>>> mystr = 'xxxSPAMxxx'`
`>>> 'SMAP' in mystr`
`True`


`>>> 'NI' in mystr`
`False`

``


conditional assignment
`a = foo if 'foo' in locals() else 'default'`

conditional printing
print("Hello windows user" if 'win' in sys.platform else "Hello linux user")
