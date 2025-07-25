import React from 'react';

import { Card, CardHeader, CardContent, Divider } from '@mui/material';

const ChildCard = ({ title, children }) => (
  <Card sx={{ padding: 0, borderColor: (theme) => theme.palette.divider }} variant="outlined">
    {title ? (
      <>
        <CardHeader title={title} />
        <Divider />{' '}
      </>
    ) : (
      ''
    )}

    <CardContent>{children}</CardContent>
  </Card>
);

ChildCard.propTypes = {
  title: PropTypes.string.isRequired,
  children: PropTypes.node,
};

export default ChildCard;
