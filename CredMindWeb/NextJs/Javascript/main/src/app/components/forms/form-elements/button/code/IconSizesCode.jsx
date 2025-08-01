import CodeDialog from '@/app/components/shared/CodeDialog'
import React from 'react'
const IconSizesCode = () => {
  return (
    <>
      <CodeDialog>
        {`
import React from 'react';
import { IconButton, Tooltip, Stack } from '@mui/material';
import { IconBell } from '@tabler/icons-react';

<Stack spacing={1} direction="row" sx={{
    justifyContent: "center"
  }}>
    <Tooltip title="Bell">
      <IconButton aria-label="small-bell">
        <IconBell width={16} />
      </IconButton>
    </Tooltip>
    <Tooltip title="Bell">
      <IconButton size="medium" aria-label="medium-bell">
        <IconBell width={19} />
      </IconButton>
    </Tooltip>
    <Tooltip title="Bell">
      <IconButton aria-label="large-bell">
        <IconBell width={21} />
      </IconButton>
    </Tooltip>
  </Stack>`}
      </CodeDialog>
    </>
  )
}

export default IconSizesCode
