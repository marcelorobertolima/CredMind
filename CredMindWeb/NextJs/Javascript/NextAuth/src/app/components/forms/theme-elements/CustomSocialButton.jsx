import React from 'react';
import { styled } from "@mui/system";
import { Button } from '@mui/material';

const CustomSocialButton = styled((props) => (
  <Button variant="outlined" size="large" color="inherit" {...props} />
))(({ theme }) => ({
  border: `1px solid ${theme.palette.divider}`,

  '&:hover': {
    color: theme.palette.primary.main,
  },
}));

export default CustomSocialButton;
