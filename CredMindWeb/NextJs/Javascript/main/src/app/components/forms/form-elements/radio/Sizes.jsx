'use client'
import React from 'react'
import { Box, Radio } from '@mui/material'

const SizesRadio = () => {
  const [selectedValue, setSelectedValue] = React.useState('a')
  const handleChange2 = (event) => {
    setSelectedValue(event.target.value)
  }

  const controlProps = (item) => ({
    checked: selectedValue === item,
    onChange: handleChange2,
    value: item,
    name: 'size-radio-button-demo',
    inputProps: { 'aria-label': item },
  })

  return (
    <Box
      sx={{
        textAlign: 'center',
      }}>
      <Radio {...controlProps('a')} size='small' />
      <Radio {...controlProps('b')} />
      <Radio
        {...controlProps('c')}
        sx={{
          '& .MuiSvgIcon-root': {
            fontSize: 28,
          },
        }}
      />
    </Box>
  )
}

export default SizesRadio
