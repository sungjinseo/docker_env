FROM mongo

ENV DATABASE=babymap
ENV USERNAME=devroot
ENV PASSWORD=devroot
ENV FILE_ONE=baby_care_facilities_info
ENV FILE_TWO=seoul_public_reserve_info

COPY ${FILE_ONE} /${FILE_ONE}.json
COPY ${FILE_TWO} /${FILE_TWO}.json

CMD mongoimport --host mongo --authenticationDatabase admin --username ${USERNAME} --password ${PASSWORD} --db ${DATABASE} --collection ${FILE_ONE} --type json --file /${FILE_ONE}.json --jsonArray && \
    mongoimport --host mongo --authenticationDatabase admin --username ${USERNAME} --password ${PASSWORD} --db ${DATABASE} --collection ${FILE_TWO} --type json --file /${FILE_TWO}.json --jsonArray
